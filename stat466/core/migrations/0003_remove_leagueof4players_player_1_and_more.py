# Generated by Django 4.2.8 on 2024-01-17 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_userextended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leagueof4players',
            name='player_1',
        ),
        migrations.RemoveField(
            model_name='leagueof4players',
            name='player_2',
        ),
        migrations.RemoveField(
            model_name='leagueof4players',
            name='player_3',
        ),
        migrations.RemoveField(
            model_name='leagueof4players',
            name='player_4',
        ),
        migrations.RemoveField(
            model_name='result4players',
            name='player_1_points',
        ),
        migrations.RemoveField(
            model_name='result4players',
            name='player_2_points',
        ),
        migrations.RemoveField(
            model_name='result4players',
            name='player_3_points',
        ),
        migrations.RemoveField(
            model_name='result4players',
            name='player_4_points',
        ),
        migrations.AddField(
            model_name='leagueof4players',
            name='team_1_player_1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='leagues_4p_t1_p1', to=settings.AUTH_USER_MODEL, verbose_name='Team 1, Player 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leagueof4players',
            name='team_1_player_2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='leagues_4p_t1_p2', to=settings.AUTH_USER_MODEL, verbose_name='Team 1, Player 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leagueof4players',
            name='team_2_player_1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='leagues_4p_t2_p1', to=settings.AUTH_USER_MODEL, verbose_name='Team 2, Player 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leagueof4players',
            name='team_2_player_2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='leagues_4p_t2_p2', to=settings.AUTH_USER_MODEL, verbose_name='Team 2, Player 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result4players',
            name='team_1_points',
            field=models.IntegerField(default=1, verbose_name='Points Team 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result4players',
            name='team_2_points',
            field=models.IntegerField(default=1, verbose_name='Points Team 2'),
            preserve_default=False,
        ),
    ]
