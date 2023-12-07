from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, Sum
from django.db.models.functions import TruncYear
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

    def get_statistic(self):
        statistic = self.results.aggregate(
            Count('id'), Sum('num_games'), Sum('player_1_points'),
            Sum('player_2_points'), Sum('player_3_points'))
        return statistic

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
        return years

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
