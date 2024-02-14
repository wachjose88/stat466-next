from django.urls import path

from core import views

urlpatterns = [
    path('', views.index, name='core.index'),
    path('league/<int:num_players>/<int:league_id>/certificate/player/<int:player_id>',
         views.certificate,
         name='core.certificate'),
    path('league/<int:num_players>/<int:league_id>/year/<int:year>/certificate/player/<int:player_id>',
         views.certificate,
         name='core.certificate'),
    path('league/<int:num_players>/<int:league_id>/year/<int:year>/month/<int:month>/certificate/player/<int:player_id>',
         views.certificate,
         name='core.certificate'),
    path('league/2/<int:league_id>', views.league_2p_years,
         name='core.league_2p_years'),
    path('league/3/<int:league_id>', views.league_3p_years,
         name='core.league_3p_years'),
    path('league/4/<int:league_id>', views.league_4p_years,
         name='core.league_4p_years'),
    path('league/3/<int:league_id>/year/<int:year>', views.league_3p_months,
         name='core.league_3p_months'),
    path('league/2/<int:league_id>/year/<int:year>', views.league_2p_months,
         name='core.league_2p_months'),
    path('league/4/<int:league_id>/year/<int:year>', views.league_4p_months,
         name='core.league_4p_months'),
    path('league/3/<int:league_id>/year/<int:year>/month/<int:month>', views.league_3p_days,
         name='core.league_3p_days'),
    path('league/2/<int:league_id>/year/<int:year>/month/<int:month>', views.league_2p_days,
         name='core.league_2p_days'),
    path('league/4/<int:league_id>/year/<int:year>/month/<int:month>', views.league_4p_days,
         name='core.league_4p_days'),
]
