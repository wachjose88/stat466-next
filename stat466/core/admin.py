from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from core.models import League, ResultTwoPlayer, ResultThreePlayer, \
    ResultFourPlayer


class LeagueAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('title',)


class ResultTwoPlayerAdmin(admin.ModelAdmin):
    list_display = ('played_at', 'num_games', 'player_1', 'player_1_points',
                    'player_2', 'player_2_points')
    list_filter = ('played_at', )


class ResultThreePlayerAdmin(admin.ModelAdmin):
    list_display = ('played_at', 'num_games', 'player_1', 'player_1_points',
                    'player_2', 'player_2_points',
                    'player_3', 'player_3_points')
    list_filter = ('played_at', )


class ResultFourPlayerAdmin(admin.ModelAdmin):
    list_display = ('played_at', 'num_games', 'player_1', 'player_1_points',
                    'player_2', 'player_2_points',
                    'player_3', 'player_3_points',
                    'player_4', 'player_4_points')
    list_filter = ('played_at', )


admin.site.register(League, LeagueAdmin)
admin.site.register(ResultTwoPlayer, ResultTwoPlayerAdmin)
admin.site.register(ResultThreePlayer, ResultThreePlayerAdmin)
admin.site.register(ResultFourPlayer, ResultFourPlayerAdmin)

# Change admin site title
admin.site.site_header = _("Stat466 Administration")
admin.site.site_title = _("Stat466 Admin")
