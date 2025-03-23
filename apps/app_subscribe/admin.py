from django.contrib import admin
from .models import UserSubscribe


@admin.register(UserSubscribe)
class UserSubscribeAdmin(admin.ModelAdmin):
    list_display = ['user', 'subscribe_type', 'created_at']