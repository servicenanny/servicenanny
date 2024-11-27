from django.forms import Textarea
from django.contrib import admin

from .models import FAQ, Review

# Register your models here.

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(FAQAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'answer':
            formfield.widget = Textarea(attrs=formfield.widget.attrs)
        return formfield

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ReviewAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'text':
            formfield.widget = Textarea(attrs=formfield.widget.attrs)
        return formfield