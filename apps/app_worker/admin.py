from django.contrib import admin

from .models import Nanny

# Register your models here.
@admin.register(Nanny)
class NannyAdmin(admin.ModelAdmin):
    ...