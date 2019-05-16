from django.contrib import admin
from .models import AllowedHost, WhiteListItem


class AllowedHostAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']


class WhiteListItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']


admin.site.register(AllowedHost, AllowedHostAdmin)
admin.site.register(WhiteListItem, WhiteListItemAdmin)
