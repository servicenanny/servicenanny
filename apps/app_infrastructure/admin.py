from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ('name', 'is_deleted')
    list_display = ('name', )
    list_filter = ('is_deleted', )
    readonly_fields = ('is_deleted', )

    def delete_model(self, request: HttpRequest, obj: City) -> None:
        """
        Delete obj by soft delete
        """
        return obj.soft_delete()