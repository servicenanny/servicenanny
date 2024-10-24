from django.contrib import admin
from django.db.models import QuerySet
from .models import Subscribe, UserSubscribe


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Отоброжаемая информация", {"fields": ('name', 'short_description')}),
        ("Конфигурация подписки", {"fields": ('client_type', 'price', 'day_range')}),
    )
    add_fieldsets = (
        ("Отоброжаемая информация", {"fields": ('name', 'short_description')}),
        ("Конфигурация подписки", {"fields": ('client_type', 'price', 'day_range')}),
    )
    list_display = ['name', 'client_type', 'day_range', 'is_deleted']
    list_filter = ['client_type', 'is_deleted', 'day_range']
    readonly_fields = ['created_by', 'created_at', 'updated_at', 'is_deleted']
    ordering = ('created_at', 'is_deleted')
    search_fields = ("name", )

    def save_model(self, request, obj: Subscribe, form, change):
        obj.created_by = request.user
        return super().save_model(request, obj, form, change)
    
    def delete_model(self, request, obj: Subscribe):
        return obj.soft_delete()
    
    def delete_queryset(self, request, queryset: QuerySet[Subscribe]):
        for obj in queryset:
            obj.soft_delete()


@admin.register(UserSubscribe)
class UserSubscribeAdmin(admin.ModelAdmin):
    list_display = ['user', 'subscribe', 'created_at']