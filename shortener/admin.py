
from django.contrib import admin
from .models import URL

@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ("short_code", "long_url", "clicks", "created_at", "last_accessed")
    search_fields = ("short_code", "long_url")
