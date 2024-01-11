from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_admin_inline_paginator.admin import TabularInlinePaginated
from core.models import LeagueOf2Players, LeagueOf3Players, LeagueOf4Players, \
    Result2Players, Result3Players, Result4Players, UserExtended


class Result2PlayersInlineAdmin(TabularInlinePaginated):
    model = Result2Players
    per_page = 10


class LeagueOf2PlayersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'player_1', 'player_2')
    list_filter = ('created_at', )
    search_fields = ('title',)
    inlines = [Result2PlayersInlineAdmin]


class Result3PlayersInlineAdmin(TabularInlinePaginated):
    model = Result3Players
    per_page = 10


class LeagueOf3PlayersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'player_1',
                    'player_2', 'player_3')
    list_filter = ('created_at', )
    search_fields = ('title',)
    inlines = [Result3PlayersInlineAdmin]


class Result4PlayersInlineAdmin(TabularInlinePaginated):
    model = Result4Players
    per_page = 10


class LeagueOf4PlayersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'player_1', 'player_2',
                    'player_3', 'player_4')
    list_filter = ('created_at', )
    search_fields = ('title',)
    inlines = [Result4PlayersInlineAdmin]


class UserExtendedAdmin(admin.ModelAdmin):
    list_display = ('user', )


admin.site.register(LeagueOf2Players, LeagueOf2PlayersAdmin)
admin.site.register(LeagueOf3Players, LeagueOf3PlayersAdmin)
admin.site.register(LeagueOf4Players, LeagueOf4PlayersAdmin)
admin.site.register(UserExtended, UserExtendedAdmin)

# Change admin site title
admin.site.site_header = _("Stat466 Administration")
admin.site.site_title = _("Stat466 Admin")
