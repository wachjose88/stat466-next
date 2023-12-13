from datetime import datetime

from django.shortcuts import render, get_object_or_404
from core.models import LeagueOf3Players, LeagueOf2Players, LeagueOf4Players


def index(request):
    leagues_2p = LeagueOf2Players.objects.all().order_by('created_at')
    leagues_3p = LeagueOf3Players.objects.all().order_by('created_at')
    leagues_4p = LeagueOf4Players.objects.all().order_by('created_at')
    params = {
        'leagues_2p': leagues_2p,
        'leagues_3p': leagues_3p,
        'leagues_4p': leagues_4p,
    }
    return render(request, 'core/index.html', params)


def league_2p_years(request, league_id):
    league = get_object_or_404(LeagueOf2Players, pk=league_id)
    params = {
        'league': league
    }
    return render(request, 'core/league_2p_years.html', params)


def league_3p_years(request, league_id):
    league = get_object_or_404(LeagueOf3Players, pk=league_id)
    statistic = league.get_statistic()
    year_statistic = league.get_year_statistic()
    win_count = year_statistic[1]
    params = {
        'league': league,
        'statistic': statistic,
        'year_statistic': year_statistic[0],
        'players': [
            (league.player_1, statistic['result'][0], win_count['player_1']),
            (league.player_2, statistic['result'][1], win_count['player_2']),
            (league.player_3, statistic['result'][2], win_count['player_3'])
        ]
    }
    return render(request, 'core/league_3p_years.html', params)


def league_4p_years(request, league_id):
    league = get_object_or_404(LeagueOf4Players, pk=league_id)
    params = {
        'league': league
    }
    return render(request, 'core/league_4p_years.html', params)


def league_3p_months(request, league_id, year):
    league = get_object_or_404(LeagueOf3Players, pk=league_id)
    statistic = league.get_month_sum_statistic(year)
    month_statistic = league.get_month_statistic(year)
    win_count = month_statistic[1]
    params = {
        'league': league,
        'statistic': statistic,
        'month_statistic': month_statistic[0],
        'year': year,
        'players': [
            (league.player_1, statistic['result'][0], win_count['player_1']),
            (league.player_2, statistic['result'][1], win_count['player_2']),
            (league.player_3, statistic['result'][2], win_count['player_3'])
        ]
    }
    return render(request, 'core/league_3p_months.html', params)


def league_3p_days(request, league_id, year, month):
    league = get_object_or_404(LeagueOf3Players, pk=league_id)
    statistic = league.get_day_sum_statistic(year, month)
    day_statistic = league.get_day_statistic(year, month)
    win_count = day_statistic[1]
    params = {
        'league': league,
        'statistic': statistic,
        'day_statistic': day_statistic[0],
        'year': year,
        'month': datetime(year, month, 1),
        'players': [
            (league.player_1, statistic['result'][0], win_count['player_1']),
            (league.player_2, statistic['result'][1], win_count['player_2']),
            (league.player_3, statistic['result'][2], win_count['player_3'])
        ]
    }
    return render(request, 'core/league_3p_days.html', params)
