# Generated by Django 4.2.8 on 2023-12-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resulttwoplayer',
            name='played_at',
            field=models.DateField(verbose_name='Played at'),
        ),
    ]
