from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from core.models import LeagueOf2Players, LeagueOf3Players, LeagueOf4Players, \
    Result2Players, Result3Players, Result4Players, UserExtended


class LeagueOf2PlayersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'player_1', 'player_2')
    list_filter = ('created_at', )
    search_fields = ('title',)


class LeagueOf3PlayersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'player_1',
                    'player_2', 'player_3')
    list_filter = ('created_at', )
    search_fields = ('title',)


class LeagueOf4PlayersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'player_1', 'player_2',
                    'player_3', 'player_4')
    list_filter = ('created_at', )
    search_fields = ('title',)


class Result2PlayersAdmin(admin.ModelAdmin):
    list_display = ('league', 'played_at', 'num_games', 'player_1_points',
                    'player_2_points')
    list_filter = ('played_at', 'league')


class Result3PlayersAdmin(admin.ModelAdmin):
    list_display = ('league', 'played_at', 'num_games', 'player_1_points',
                    'player_2_points', 'player_3_points')
    list_filter = ('played_at', 'league')


class Result4PlayersAdmin(admin.ModelAdmin):
    list_display = ('league', 'played_at', 'num_games', 'player_1_points',
                    'player_2_points', 'player_3_points', 'player_4_points')
    list_filter = ('played_at', 'league')


class UserExtendedAdmin(admin.ModelAdmin):
    list_display = ('user', )


admin.site.register(LeagueOf2Players, LeagueOf2PlayersAdmin)
admin.site.register(LeagueOf3Players, LeagueOf3PlayersAdmin)
admin.site.register(LeagueOf4Players, LeagueOf4PlayersAdmin)
admin.site.register(Result2Players, Result2PlayersAdmin)
admin.site.register(Result3Players, Result3PlayersAdmin)
admin.site.register(Result4Players, Result4PlayersAdmin)
admin.site.register(UserExtended, UserExtendedAdmin)

# Change admin site title
admin.site.site_header = _("Stat466 Administration")
admin.site.site_title = _("Stat466 Admin")
