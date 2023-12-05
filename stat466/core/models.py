from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class League(models.Model):

    title = models.CharField(
        max_length=128,
        verbose_name=_('Title')
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Created at')
    )

    members = models.ManyToManyField(
        User,
        related_name='leagues',
        verbose_name=_('Members')
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = _('League')
        verbose_name_plural = _('Leagues')


class ResultTwoPlayer(models.Model):

    played_at = models.DateField(
        verbose_name=_('Played at')
    )

    num_games = models.IntegerField(
        verbose_name=_('Number of games')
    )

    player_1 = models.ForeignKey(
        User,
        related_name='results_two_player_1',
        on_delete=models.CASCADE,
        verbose_name=_('Player 1')
    )

    player_1_points = models.IntegerField(
        verbose_name=_('Points Player 1')
    )

    player_2 = models.ForeignKey(
        User,
        related_name='results_two_player_2',
        on_delete=models.CASCADE,
        verbose_name=_('Player 2')
    )

    player_2_points = models.IntegerField(
        verbose_name=_('Points Player 2')
    )

    def __str__(self):
        return f'Result 2P: {self.played_at}'

    class Meta:
        verbose_name = _('Result of a 2 Player game')
        verbose_name_plural = _('Results of 2 Player games')


class ResultThreePlayer(models.Model):

    played_at = models.DateField(
        verbose_name=_('Played at')
    )

    num_games = models.IntegerField(
        verbose_name=_('Number of games')
    )

    player_1 = models.ForeignKey(
        User,
        related_name='results_three_player_1',
        on_delete=models.CASCADE,
        verbose_name=_('Player 1')
    )

    player_1_points = models.IntegerField(
        verbose_name=_('Points Player 1')
    )

    player_2 = models.ForeignKey(
        User,
        related_name='results_three_player_2',
        on_delete=models.CASCADE,
        verbose_name=_('Player 2')
    )

    player_2_points = models.IntegerField(
        verbose_name=_('Points Player 2')
    )

    player_3 = models.ForeignKey(
        User,
        related_name='results_three_player_3',
        on_delete=models.CASCADE,
        verbose_name=_('Player 3')
    )

    player_3_points = models.IntegerField(
        verbose_name=_('Points Player 3')
    )

    def __str__(self):
        return f'Result 3P: {self.played_at}'

    class Meta:
        verbose_name = _('Result of a 3 Player game')
        verbose_name_plural = _('Results of 3 Player games')


class ResultFourPlayer(models.Model):

    played_at = models.DateField(
        verbose_name=_('Played at')
    )

    num_games = models.IntegerField(
        verbose_name=_('Number of games')
    )

    player_1 = models.ForeignKey(
        User,
        related_name='results_four_player_1',
        on_delete=models.CASCADE,
        verbose_name=_('Player 1')
    )

    player_1_points = models.IntegerField(
        verbose_name=_('Points Player 1')
    )

    player_2 = models.ForeignKey(
        User,
        related_name='results_four_player_2',
        on_delete=models.CASCADE,
        verbose_name=_('Player 2')
    )

    player_2_points = models.IntegerField(
        verbose_name=_('Points Player 2')
    )

    player_3 = models.ForeignKey(
        User,
        related_name='results_four_player_3',
        on_delete=models.CASCADE,
        verbose_name=_('Player 3')
    )

    player_3_points = models.IntegerField(
        verbose_name=_('Points Player 3')
    )

    player_4 = models.ForeignKey(
        User,
        related_name='results_four_player_4',
        on_delete=models.CASCADE,
        verbose_name=_('Player 3')
    )

    player_4_points = models.IntegerField(
        verbose_name=_('Points Player 4')
    )

    def __str__(self):
        return f'Result 3P: {self.played_at}'

    class Meta:
        verbose_name = _('Result of a 4 Player game')
        verbose_name_plural = _('Results of 4 Player games')
