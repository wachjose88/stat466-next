from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, Sum
from django.db.models.functions import TruncYear, TruncMonth, TruncDay
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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

    @classmethod
    def sort_results(cls, points_1, points_2, points_3):
        result = [
            ['player_1', points_1, 0],
            ['player_2', points_2, 0],
            ['player_3', points_3, 0],
        ]
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
            'result': result
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
            'result': result
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
        combined = []
        for year in years:
            result = self.sort_results(
                year['sum_player_1'], year['sum_player_2'], year['sum_player_3']
            )
            combine = {
                'year': year['year'],
                'num_results': year['num_results'],
                'sum_games': year['sum_games'],
                'result': result
            }
            combined.append(combine)
        return combined

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
        combined = []
        for month in months:
            result = self.sort_results(
                month['sum_player_1'], month['sum_player_2'], month['sum_player_3']
            )
            combine = {
                'month': month['month'],
                'num_results': month['num_results'],
                'sum_games': month['sum_games'],
                'result': result
            }
            combined.append(combine)
        return combined

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
        combined = []
        for day in days:
            result = self.sort_results(
                day['sum_player_1'], day['sum_player_2'], day['sum_player_3']
            )
            combine = {
                'day': day['day'],
                'num_results': day['num_results'],
                'sum_games': day['sum_games'],
                'result': result
            }
            combined.append(combine)
        return combined

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

    player_1 = models.ForeignKey(
        User,
        related_name='leagues_4p_p1',
        on_delete=models.CASCADE,
        verbose_name=_('Player 1')
    )

    player_2 = models.ForeignKey(
        User,
        related_name='leagues_4p_p2',
        on_delete=models.CASCADE,
        verbose_name=_('Player 2')
    )

    player_3 = models.ForeignKey(
        User,
        related_name='leagues_4p_p3',
        on_delete=models.CASCADE,
        verbose_name=_('Player 3')
    )

    player_4 = models.ForeignKey(
        User,
        related_name='leagues_4p_p4',
        on_delete=models.CASCADE,
        verbose_name=_('Player 4')
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

    player_1_points = models.IntegerField(
        verbose_name=_('Points Player 1')
    )

    player_2_points = models.IntegerField(
        verbose_name=_('Points Player 2')
    )

    player_3_points = models.IntegerField(
        verbose_name=_('Points Player 3')
    )

    player_4_points = models.IntegerField(
        verbose_name=_('Points Player 4')
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
