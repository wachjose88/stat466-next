from datetime import datetime, date

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from core.models import LeagueOf3Players, LeagueOf2Players, LeagueOf4Players
from core.renderers import render_to_pdf


def certificate(request, num_players, league_id, player_id,
                year=None, month=None):
    player = get_object_or_404(User, pk=player_id)

    if num_players == 2:
        league = get_object_or_404(LeagueOf2Players, pk=league_id)
        params = {
            'league': league,
        }
    elif num_players == 3:
        league = get_object_or_404(LeagueOf3Players, pk=league_id)
        player_num = league.get_player_num(player)
        if year is None and month is None:
            statistic = league.get_statistic()
            subtitle = _('Overall')
        elif year is not None and month is None:
            statistic = league.get_month_sum_statistic(year)
            subtitle = _('Year:') + f' {year}'
        elif year is not None and month is not None:
            statistic = league.get_day_sum_statistic(year, month)
            subtitle = _('Month:') + f' {month} {year}'
        result = sorted(statistic['result'], key=lambda rank: rank[2])
        for p in result:
            if p[0] == 'player_1':
                p.append(league.player_1)
            elif p[0] == 'player_2':
                p.append(league.player_2)
            elif p[0] == 'player_3':
                p.append(league.player_3)
        params = {
            'league': league,
            'league_type': _('League of 3 Players'),
            'player': player,
            'rank': statistic['result'][player_num][2],
            'points': statistic['result'][player_num][1],
            'statistic': statistic,
            'result': result,
            'subtitle': subtitle
        }
    elif num_players == 4:
        league = get_object_or_404(LeagueOf4Players, pk=league_id)
        params = {
            'league': league,
        }
    return render_to_pdf('core/certificate.html', params)


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
    statistic = league.get_statistic()
    year_statistic = league.get_year_statistic()
    win_count = year_statistic[1]
    params = {
        'league': league,
        'statistic': statistic,
        'year_statistic': year_statistic[0],
        'players': [
            (league.player_1, statistic['result'][0], win_count['player_1']),
            (league.player_2, statistic['result'][1], win_count['player_2'])
        ]
    }
    return render(request, 'core/league_2p_years.html', params)


def league_2p_months(request, league_id, year):
    league = get_object_or_404(LeagueOf2Players, pk=league_id)
    statistic = league.get_month_sum_statistic(year)
    month_statistic = league.get_month_statistic(year)
    win_count = month_statistic[1]

    half_year = [
        (_('First half year'), league.get_month_period_statistic(
            date(year, 1, 1), date(year, 6, 30))),
        (_('Second half year'), league.get_month_period_statistic(
            date(year, 7, 1), date(year, 12, 31)))
    ]

    quarter_year = [
        (_('First quarter year'), league.get_month_period_statistic(
            date(year, 1, 1), date(year, 3, 31))),
        (_('Second quarter year'), league.get_month_period_statistic(
            date(year, 4, 1), date(year, 6, 30))),
        (_('Third quarter year'), league.get_month_period_statistic(
            date(year, 7, 1), date(year, 9, 30))),
        (_('Fourth quarter year'), league.get_month_period_statistic(
            date(year, 10, 1), date(year, 12, 31))),
    ]

    params = {
        'league': league,
        'statistic': statistic,
        'month_statistic': month_statistic[0],
        'year': year,
        'players': [
            (league.player_1, statistic['result'][0], win_count['player_1']),
            (league.player_2, statistic['result'][1], win_count['player_2'])
        ],
        'half_year': half_year,
        'quarter_year': quarter_year
    }
    return render(request, 'core/league_2p_months.html', params)


def league_2p_days(request, league_id, year, month):
    league = get_object_or_404(LeagueOf2Players, pk=league_id)
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
            (league.player_2, statistic['result'][1], win_count['player_2'])
        ]
    }
    return render(request, 'core/league_2p_days.html', params)


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
            (league.player_1, statistic['result'][0], win_count['player_1'],
             reverse('core.certificate', kwargs={
                 'num_players': 3, 'league_id': league_id,
                 'player_id': league.player_1.id
             })),
            (league.player_2, statistic['result'][1], win_count['player_2'],
             reverse('core.certificate', kwargs={
                 'num_players': 3, 'league_id': league_id,
                 'player_id': league.player_2.id
             })),
            (league.player_3, statistic['result'][2], win_count['player_3'],
             reverse('core.certificate', kwargs={
                 'num_players': 3, 'league_id': league_id,
                 'player_id': league.player_3.id
             }))
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

    half_year = [
        (_('First half year'), league.get_month_period_statistic(
            date(year, 1, 1), date(year, 6, 30))),
        (_('Second half year'), league.get_month_period_statistic(
            date(year, 7, 1), date(year, 12, 31)))
    ]

    quarter_year = [
        (_('First quarter year'), league.get_month_period_statistic(
            date(year, 1, 1), date(year, 3, 31))),
        (_('Second quarter year'), league.get_month_period_statistic(
            date(year, 4, 1), date(year, 6, 30))),
        (_('Third quarter year'), league.get_month_period_statistic(
            date(year, 7, 1), date(year, 9, 30))),
        (_('Fourth quarter year'), league.get_month_period_statistic(
            date(year, 10, 1), date(year, 12, 31))),
    ]

    params = {
        'league': league,
        'statistic': statistic,
        'month_statistic': month_statistic[0],
        'year': year,
        'players': [
            (league.player_1, statistic['result'][0], win_count['player_1'],
             reverse('core.certificate', kwargs={
                 'num_players': 3, 'league_id': league_id,
                 'player_id': league.player_1.id, 'year': year
             })),
            (league.player_2, statistic['result'][1], win_count['player_2'],
             reverse('core.certificate', kwargs={
                 'num_players': 3, 'league_id': league_id,
                 'player_id': league.player_2.id, 'year': year
             })),
            (league.player_3, statistic['result'][2], win_count['player_3'],
             reverse('core.certificate', kwargs={
                 'num_players': 3, 'league_id': league_id,
                 'player_id': league.player_3.id, 'year': year
             }))
        ],
        'half_year': half_year,
        'quarter_year': quarter_year
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
            (league.player_1, statistic['result'][0], win_count['player_1'],
             reverse('core.certificate', kwargs={
                 'num_players': 3, 'league_id': league_id,
                 'player_id': league.player_1.id, 'year': year, 'month': month
             })),
            (league.player_2, statistic['result'][1], win_count['player_2'],
             reverse('core.certificate', kwargs={
                 'num_players': 3, 'league_id': league_id,
                 'player_id': league.player_2.id, 'year': year, 'month': month
             })),
            (league.player_3, statistic['result'][2], win_count['player_3'],
             reverse('core.certificate', kwargs={
                 'num_players': 3, 'league_id': league_id,
                 'player_id': league.player_3.id, 'year': year, 'month': month
             }))
        ]
    }
    return render(request, 'core/league_3p_days.html', params)
