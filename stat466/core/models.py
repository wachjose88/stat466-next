from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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
