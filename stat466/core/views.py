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
    params = {
        'league': league,
        'statistic': league.get_statistic(),
        'year_statistic': league.get_year_statistic()
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
    params = {
        'league': league,
        'statistic': league.get_month_sum_statistic(year),
        'month_statistic': league.get_month_statistic(year),
        'year': year
    }
    return render(request, 'core/league_3p_months.html', params)
