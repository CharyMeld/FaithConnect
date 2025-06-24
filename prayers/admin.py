from django.contrib import admin
from .models import PrayerRequest, PrayerResponse

@admin.register(PrayerRequest)
class PrayerRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'message', 'user__username')

@admin.register(PrayerResponse)
class PrayerResponseAdmin(admin.ModelAdmin):
    list_display = ('prayer_request', 'sender', 'is_private', 'created_at')
    search_fields = ('message', 'sender__username')

