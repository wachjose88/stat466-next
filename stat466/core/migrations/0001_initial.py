# Generated by Django 4.2.8 on 2023-12-05 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultTwoPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
                ('num_games', models.IntegerField(verbose_name='Number of games')),
                ('player_1_points', models.IntegerField(verbose_name='Points Player 1')),
                ('player_2_points', models.IntegerField(verbose_name='Points Player 2')),
                ('player_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results_two_player_1', to=settings.AUTH_USER_MODEL, verbose_name='Player 1')),
                ('player_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results_two_player_2', to=settings.AUTH_USER_MODEL, verbose_name='Player 2')),
            ],
            options={
                'verbose_name': 'Result of a 2 Player game',
                'verbose_name_plural': 'Results of 2 Player games',
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
                ('members', models.ManyToManyField(related_name='leagues', to=settings.AUTH_USER_MODEL, verbose_name='Members')),
            ],
            options={
                'verbose_name': 'League',
                'verbose_name_plural': 'Leagues',
            },
        ),
    ]