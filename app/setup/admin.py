from django.contrib import admin
from django.http.request import HttpRequest

from setup.models import MenuLink, Setup


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path'
    list_display_links = 'id', 'text', 'url_or_path'
    search_fields = 'id', 'text', 'url_or_path'


@admin.register(Setup)
class SetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description'
    list_display_link = 'title', 'description'

    @staticmethod
    def has_add_permission(request) -> bool:
        return not Setup.objects.exists()
