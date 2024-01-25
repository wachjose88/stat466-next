from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, Sum
from django.db.models.functions import TruncYear, TruncMonth, TruncDay
from django.templatetags.static import static
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.staticfiles import finders


def custom_user_str(self):
    if self.first_name is None or self.last_name is None:
        return str(self.username)
    return f'{self.first_name} {self.last_name}'

User.add_to_class("__str__", custom_user_str)


class LeagueOf2Players(models.Model):

    title = models.CharField(
        max_length=128,
        verbose_name=_('Title')
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Created at')
    )

    player_1 = models.ForeignKey(
        User,
        related_name='leagues_2p_p1',
        on_delete=models.CASCADE,
        verbose_name=_('Player 1')
    )

    player_2 = models.ForeignKey(
        User,
        related_name='leagues_2p_p2',
        on_delete=models.CASCADE,
        verbose_name=_('Player 2')
    )

    @classmethod
    def sort_results(cls, points_1, points_2):
        result = [
            ['player_1', points_1, 0, 0],
            ['player_2', points_2, 0, 0]
        ]
        if None in [points_1, points_2]:
            result = [
                ['player_1', 0, 0, 0],
                ['player_2', 0, 0, 0]
            ]
            return result
        result = sorted(result, key=lambda player: player[1])
        for i in range(0, 2):
            result[i][2] = i + 1
            if i > 0:
                if result[i-1][1] == result[i][1]:
                    result[i][2] = result[i-1][2]
        result = sorted(result, key=lambda player: player[0])
        return result

    def get_statistic(self):
        statistic = self.results.aggregate(
            Count('id'), Sum('num_games'), Sum('player_1_points'),
            Sum('player_2_points'))
        result = self.sort_results(statistic['player_1_points__sum'],
                                   statistic['player_2_points__sum'])
        combined = {
            'num_games': statistic['num_games__sum'],
            'num_results': statistic['id__count'],
            'result': result,
            'avg_games_per_result': round(statistic['num_games__sum'] /
                statistic['id__count'], 2) if statistic['id__count'] > 0 else 0
        }
        return combined

    def get_month_sum_statistic(self, year):
        statistic = self.results.filter(played_at__year=year).aggregate(
            Count('id'), Sum('num_games'), Sum('player_1_points'),
            Sum('player_2_points'))
        result = self.sort_results(statistic['player_1_points__sum'],
                                   statistic['player_2_points__sum'])
        combined = {
            'num_games': statistic['num_games__sum'],
            'num_results': statistic['id__count'],
            'result': result,
            'avg_games_per_result': round(statistic['num_games__sum'] /
                statistic['id__count'], 2) if statistic['id__count'] > 0 else 0
        }
        return combined

    def get_month_period_statistic(self, from_date, to_date):
        statistic = self.results.filter(played_at__gte=from_date,
                                        played_at__lte=to_date).aggregate(
            Count('id'), Sum('num_games'), Sum('player_1_points'),
            Sum('player_2_points'))
        result = self.sort_results(statistic['player_1_points__sum'],
                                   statistic['player_2_points__sum'])
        combined = {
            'num_games': statistic['num_games__sum']
                if statistic['num_games__sum'] is not None else 0,
            'num_results': statistic['id__count'],
            'result': result
        }
        return combined

    def get_day_sum_statistic(self, year, month):
        statistic = self.results.filter(played_at__year=year,
                                        played_at__month=month).aggregate(
            Count('id'), Sum('num_games'), Sum('player_1_points'),
            Sum('player_2_points'))
        result = self.sort_results(statistic['player_1_points__sum'],
                                   statistic['player_2_points__sum'])
        combined = {
            'num_games': statistic['num_games__sum'],
            'num_results': statistic['id__count'],
            'result': result,
            'avg_games_per_result': round(statistic['num_games__sum'] /
                statistic['id__count'], 2) if statistic['id__count'] > 0 else 0
        }
        return combined

    def get_day_statistic(self, year, month):
        days = self.results.filter(played_at__year=year, played_at__month=month)\
            .annotate(day=TruncDay('played_at'))\
            .values('day')\
            .annotate(
                num_results=Count('id'),
                sum_games=Sum('num_games'),
                sum_player_1=Sum('player_1_points'),
                sum_player_2=Sum('player_2_points')
            )\
            .values('day', 'num_results', 'sum_games', 'sum_player_1',
                    'sum_player_2')
        win_count = {
            'player_1': 0,
            'player_2': 0
        }
        combined = []
        for day in days:
            result = self.sort_results(
                day['sum_player_1'], day['sum_player_2']
            )
            if len(combined) > 0:
                result[0][3] = combined[-1]['result'][0][3] + result[0][1]
                result[1][3] = combined[-1]['result'][1][3] + result[1][1]
            else:
                result[0][3] = result[0][1]
                result[1][3] = result[1][1]
            if result[0][2] == 1:
                win_count['player_1'] += 1
            if result[1][2] == 1:
                win_count['player_2'] += 1
            combine = {
                'day': day['day'],
                'num_results': day['num_results'],
                'sum_games': day['sum_games'],
                'result': result
            }
            combined.append(combine)
        return combined, win_count

    def get_month_statistic(self, year):
        months = self.results.filter(played_at__year=year)\
            .annotate(month=TruncMonth('played_at'))\
            .values('month')\
            .annotate(
                num_results=Count('id'),
                sum_games=Sum('num_games'),
                sum_player_1=Sum('player_1_points'),
                sum_player_2=Sum('player_2_points')
            )\
            .values('month', 'num_results', 'sum_games', 'sum_player_1',
                    'sum_player_2')
        win_count = {
            'player_1': 0,
            'player_2': 0
        }
        combined = []
        for month in months:
            result = self.sort_results(
                month['sum_player_1'], month['sum_player_2']
            )
            if len(combined) > 0:
                result[0][3] = combined[-1]['result'][0][3] + result[0][1]
                result[1][3] = combined[-1]['result'][1][3] + result[1][1]
            else:
                result[0][3] = result[0][1]
                result[1][3] = result[1][1]
            if result[0][2] == 1:
                win_count['player_1'] += 1
            if result[1][2] == 1:
                win_count['player_2'] += 1
            combine = {
                'month': month['month'],
                'num_results': month['num_results'],
                'sum_games': month['sum_games'],
                'result': result
            }
            combined.append(combine)
        return combined, win_count

    def get_year_statistic(self):
        years = self.results.annotate(year=TruncYear('played_at'))\
            .values('year')\
            .annotate(
                num_results=Count('id'),
                sum_games=Sum('num_games'),
                sum_player_1=Sum('player_1_points'),
                sum_player_2=Sum('player_2_points')
            )\
            .values('year', 'num_results', 'sum_games', 'sum_player_1',
                    'sum_player_2')
        win_count = {
            'player_1': 0,
            'player_2': 0
        }
        combined = []
        for year in years:
            result = self.sort_results(
                year['sum_player_1'], year['sum_player_2']
            )
            if result[0][2] == 1:
                win_count['player_1'] += 1
            if result[1][2] == 1:
                win_count['player_2'] += 1
            combine = {
                'year': year['year'],
                'num_results': year['num_results'],
                'sum_games': year['sum_games'],
                'result': result
            }
            combined.append(combine)
        return combined, win_count

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = _('League of 2 Players')
        verbose_name_plural = _('Leagues of 2 Players')


class LeagueOf3Players(models.Model):

    title = models.CharField(
        max_length=128,
        verbose_name=_('Title')
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Created at')
    )

    player_1 = models.ForeignKey(
        User,
        related_name='leagues_3p_p1',
        on_delete=models.CASCADE,
        verbose_name=_('Player 1')
    )

    player_2 = models.ForeignKey(
        User,
        related_name='leagues_3p_p2',
        on_delete=models.CASCADE,
        verbose_name=_('Player 2')
    )

    player_3 = models.ForeignKey(
        User,
        related_name='leagues_3p_p3',
        on_delete=models.CASCADE,
        verbose_name=_('Player 3')
    )

    def get_player_num(self, player):
        if self.player_1 == player:
            return 0
        elif self.player_2 == player:
            return 1
        elif self.player_3 == player:
            return 2

    @classmethod
    def sort_results(cls, points_1, points_2, points_3):
        result = [
            ['player_1', points_1, 0, 0],
            ['player_2', points_2, 0, 0],
            ['player_3', points_3, 0, 0],
        ]
        if None in [points_1, points_2, points_3]:
            result = [
                ['player_1', 0, 0, 0],
                ['player_2', 0, 0, 0],
                ['player_3', 0, 0, 0],
            ]
            return result
        result = sorted(result, key=lambda player: player[1])
        for i in range(0, 3):
            result[i][2] = i + 1
            if i > 0:
                if result[i-1][1] == result[i][1]:
                    result[i][2] = result[i-1][2]
        result = sorted(result, key=lambda player: player[0])
        return result

    def get_statistic(self):
        statistic = self.results.aggregate(
            Count('id'), Sum('num_games'), Sum('player_1_points'),
            Sum('player_2_points'), Sum('player_3_points'))
        result = self.sort_results(statistic['player_1_points__sum'],
                                   statistic['player_2_points__sum'],
                                   statistic['player_3_points__sum'])
        combined = {
            'num_games': statistic['num_games__sum'],
            'num_results': statistic['id__count'],
            'result': result,
            'avg_games_per_result': round(statistic['num_games__sum'] /
                statistic['id__count'], 2) if statistic['id__count'] > 0 else 0
        }
        return combined

    def get_month_sum_statistic(self, year):
        statistic = self.results.filter(played_at__year=year).aggregate(
            Count('id'), Sum('num_games'), Sum('player_1_points'),
            Sum('player_2_points'), Sum('player_3_points'))
        result = self.sort_results(statistic['player_1_points__sum'],
                                   statistic['player_2_points__sum'],
                                   statistic['player_3_points__sum'])
        combined = {
            'num_games': statistic['num_games__sum'],
            'num_results': statistic['id__count'],
            'result': result,
            'avg_games_per_result': round(statistic['num_games__sum'] /
                statistic['id__count'], 2) if statistic['id__count'] > 0 else 0
        }
        return combined

    def get_day_sum_statistic(self, year, month):
        statistic = self.results.filter(played_at__year=year,
                                        played_at__month=month).aggregate(
            Count('id'), Sum('num_games'), Sum('player_1_points'),
            Sum('player_2_points'), Sum('player_3_points'))
        result = self.sort_results(statistic['player_1_points__sum'],
                                   statistic['player_2_points__sum'],
                                   statistic['player_3_points__sum'])
        combined = {
            'num_games': statistic['num_games__sum'],
            'num_results': statistic['id__count'],
            'result': result,
            'avg_games_per_result': round(statistic['num_games__sum'] /
                statistic['id__count'], 2) if statistic['id__count'] > 0 else 0
        }
        return combined

    def get_month_period_statistic(self, from_date, to_date):
        statistic = self.results.filter(played_at__gte=from_date,
                                        played_at__lte=to_date).aggregate(
            Count('id'), Sum('num_games'), Sum('player_1_points'),
            Sum('player_2_points'), Sum('player_3_points'))
        result = self.sort_results(statistic['player_1_points__sum'],
                                   statistic['player_2_points__sum'],
                                   statistic['player_3_points__sum'])
        combined = {
            'num_games': statistic['num_games__sum']
                if statistic['num_games__sum'] is not None else 0,
            'num_results': statistic['id__count'],
            'result': result
        }
        return combined

    def get_year_statistic(self):
        years = self.results.annotate(year=TruncYear('played_at'))\
            .values('year')\
            .annotate(
                num_results=Count('id'),
                sum_games=Sum('num_games'),
                sum_player_1=Sum('player_1_points'),
                sum_player_2=Sum('player_2_points'),
                sum_player_3=Sum('player_3_points')
            )\
            .values('year', 'num_results', 'sum_games', 'sum_player_1',
                    'sum_player_2', 'sum_player_3')
        win_count = {
            'player_1': 0,
            'player_2': 0,
            'player_3': 0,
        }
        combined = []
        for year in years:
            result = self.sort_results(
                year['sum_player_1'], year['sum_player_2'], year['sum_player_3']
            )
            if result[0][2] == 1:
                win_count['player_1'] += 1
            if result[1][2] == 1:
                win_count['player_2'] += 1
            if result[2][2] == 1:
                win_count['player_3'] += 1
            combine = {
                'year': year['year'],
                'num_results': year['num_results'],
                'sum_games': year['sum_games'],
                'result': result
            }
            combined.append(combine)
        return combined, win_count

    def get_month_statistic(self, year):
        months = self.results.filter(played_at__year=year)\
            .annotate(month=TruncMonth('played_at'))\
            .values('month')\
            .annotate(
                num_results=Count('id'),
                sum_games=Sum('num_games'),
                sum_player_1=Sum('player_1_points'),
                sum_player_2=Sum('player_2_points'),
                sum_player_3=Sum('player_3_points')
            )\
            .values('month', 'num_results', 'sum_games', 'sum_player_1',
                    'sum_player_2', 'sum_player_3')
        win_count = {
            'player_1': 0,
            'player_2': 0,
            'player_3': 0,
        }
        combined = []
        for month in months:
            result = self.sort_results(
                month['sum_player_1'], month['sum_player_2'], month['sum_player_3']
            )
            if len(combined) > 0:
                result[0][3] = combined[-1]['result'][0][3] + result[0][1]
                result[1][3] = combined[-1]['result'][1][3] + result[1][1]
                result[2][3] = combined[-1]['result'][2][3] + result[2][1]
            else:
                result[0][3] = result[0][1]
                result[1][3] = result[1][1]
                result[2][3] = result[2][1]
            if result[0][2] == 1:
                win_count['player_1'] += 1
            if result[1][2] == 1:
                win_count['player_2'] += 1
            if result[2][2] == 1:
                win_count['player_3'] += 1
            combine = {
                'month': month['month'],
                'num_results': month['num_results'],
                'sum_games': month['sum_games'],
                'result': result
            }
            combined.append(combine)
        return combined, win_count

    def get_day_statistic(self, year, month):
        days = self.results.filter(played_at__year=year, played_at__month=month)\
            .annotate(day=TruncDay('played_at'))\
            .values('day')\
            .annotate(
                num_results=Count('id'),
                sum_games=Sum('num_games'),
                sum_player_1=Sum('player_1_points'),
                sum_player_2=Sum('player_2_points'),
                sum_player_3=Sum('player_3_points')
            )\
            .values('day', 'num_results', 'sum_games', 'sum_player_1',
                    'sum_player_2', 'sum_player_3')
        win_count = {
            'player_1': 0,
            'player_2': 0,
            'player_3': 0,
        }
        combined = []
        for day in days:
            result = self.sort_results(
                day['sum_player_1'], day['sum_player_2'], day['sum_player_3']
            )
            if len(combined) > 0:
                result[0][3] = combined[-1]['result'][0][3] + result[0][1]
                result[1][3] = combined[-1]['result'][1][3] + result[1][1]
                result[2][3] = combined[-1]['result'][2][3] + result[2][1]
            else:
                result[0][3] = result[0][1]
                result[1][3] = result[1][1]
                result[2][3] = result[2][1]
            if result[0][2] == 1:
                win_count['player_1'] += 1
            if result[1][2] == 1:
                win_count['player_2'] += 1
            if result[2][2] == 1:
                win_count['player_3'] += 1
            combine = {
                'day': day['day'],
                'num_results': day['num_results'],
                'sum_games': day['sum_games'],
                'result': result
            }
            combined.append(combine)
        return combined, win_count

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = _('League of 3 Players')
        verbose_name_plural = _('Leagues of 3 Players')


class LeagueOf4Players(models.Model):

    title = models.CharField(
        max_length=128,
        verbose_name=_('Title')
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Created at')
    )

    team_1_player_1 = models.ForeignKey(
        User,
        related_name='leagues_4p_t1_p1',
        on_delete=models.CASCADE,
        verbose_name=_('Team 1, Player 1')
    )

    team_1_player_2 = models.ForeignKey(
        User,
        related_name='leagues_4p_t1_p2',
        on_delete=models.CASCADE,
        verbose_name=_('Team 1, Player 2')
    )

    team_2_player_1 = models.ForeignKey(
        User,
        related_name='leagues_4p_t2_p1',
        on_delete=models.CASCADE,
        verbose_name=_('Team 2, Player 1')
    )

    team_2_player_2 = models.ForeignKey(
        User,
        related_name='leagues_4p_t2_p2',
        on_delete=models.CASCADE,
        verbose_name=_('Team 2, Player 2')
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = _('League of 4 Players')
        verbose_name_plural = _('Leagues of 4 Players')


class Result2Players(models.Model):

    played_at = models.DateField(
        verbose_name=_('Played at')
    )

    num_games = models.IntegerField(
        verbose_name=_('Number of games')
    )

    player_1_points = models.IntegerField(
        verbose_name=_('Points Player 1')
    )

    player_2_points = models.IntegerField(
        verbose_name=_('Points Player 2')
    )

    league = models.ForeignKey(
        LeagueOf2Players,
        related_name='results',
        on_delete=models.CASCADE,
        verbose_name=_('League')
    )

    def __str__(self):
        return f'Result 2P: {self.played_at}'

    class Meta:
        verbose_name = _('Result of a 2 Player game')
        verbose_name_plural = _('Results of 2 Player games')


class Result3Players(models.Model):

    played_at = models.DateField(
        verbose_name=_('Played at')
    )

    num_games = models.IntegerField(
        verbose_name=_('Number of games')
    )

    player_1_points = models.IntegerField(
        verbose_name=_('Points Player 1')
    )

    player_2_points = models.IntegerField(
        verbose_name=_('Points Player 2')
    )

    player_3_points = models.IntegerField(
        verbose_name=_('Points Player 3')
    )

    league = models.ForeignKey(
        LeagueOf3Players,
        related_name='results',
        on_delete=models.CASCADE,
        verbose_name=_('League')
    )

    def __str__(self):
        return f'Result 3P: {self.played_at}'

    class Meta:
        verbose_name = _('Result of a 3 Player game')
        verbose_name_plural = _('Results of 3 Player games')


class Result4Players(models.Model):

    played_at = models.DateField(
        verbose_name=_('Played at')
    )

    num_games = models.IntegerField(
        verbose_name=_('Number of games')
    )

    team_1_points = models.IntegerField(
        verbose_name=_('Points Team 1')
    )

    team_2_points = models.IntegerField(
        verbose_name=_('Points Team 2')
    )

    league = models.ForeignKey(
        LeagueOf4Players,
        related_name='results',
        on_delete=models.CASCADE,
        verbose_name=_('League')
    )

    def __str__(self):
        return f'Result 4P: {self.played_at}'

    class Meta:
        verbose_name = _('Result of a 4 Player game')
        verbose_name_plural = _('Results of 4 Player games')


class UserExtended(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='extended',
        verbose_name=_('User'),
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        verbose_name=_('Image'),
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.user}'

    def get_image_path(self):
        try:
            if self.image is not None:
                return self.image.path
        except ValueError:
            pass
        url = finders.find('core/images/user-bg.png')
        return url

    def get_image(self):
        try:
            if self.image is not None:
                return self.image.url
        except ValueError:
            pass
        url = static('core/images/user.png')
        return url

    class Meta:
        verbose_name = _('User Extended')
        verbose_name_plural = _('Users Extended')


def custom_user_get_extended(self):
    if not hasattr(self, 'extended'):
        self.extended = UserExtended.objects.create(user=self, image=None)
    return self.extended


User.add_to_class('get_extended', custom_user_get_extended)
