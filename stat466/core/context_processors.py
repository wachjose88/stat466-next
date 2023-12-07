from core.models import LeagueOf2Players, LeagueOf4Players, LeagueOf3Players


def list_leagues(request):
    return {
        'list_leagues_of_2p':
            LeagueOf2Players.objects.all().order_by('created_at'),
        'list_leagues_of_3p':
            LeagueOf3Players.objects.all().order_by('created_at'),
        'list_leagues_of_4p':
            LeagueOf4Players.objects.all().order_by('created_at'),
    }
