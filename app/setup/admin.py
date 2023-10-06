from django.contrib import admin

from setup.models import MenuLink, Setup


class MenuLinkInline(admin.TabularInline):
    model = MenuLink
    extra = 1


@admin.register(Setup)
class SetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    list_display_link = 'title', 'description',
    inlines = MenuLinkInline,

    @staticmethod
    def has_add_permission(request) -> bool:
        return not Setup.objects.exists()
