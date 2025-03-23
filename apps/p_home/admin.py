from django import forms
from django.forms import Textarea, ValidationError
from django.contrib import admin

from .models import FAQ, Review, AudioReview, VideoReview

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
    

class AudioReviewForm(forms.ModelForm):
    class Meta:
        model = AudioReview
        fields = ('number', 'from_client', 'preview', 'file')

    def clean_number(self):
        number = self.cleaned_data['number']
        if VideoReview.objects.filter(number = number).exists() or AudioReview.objects.filter(number = number).exists():
            raise ValidationError(f'Порядковый номер не может повторяться. Номер {number} уже занят')
        return number
    

@admin.register(AudioReview)
class AudioReviewAdmin(admin.ModelAdmin):
    form = AudioReviewForm


class VideoReviewForm(forms.ModelForm):
    class Meta:
        model = AudioReview
        fields = ('number', 'from_client', 'preview', 'file')

    def clean_number(self):
        number = self.cleaned_data['number']
        if VideoReview.objects.filter(number = number).exists() or AudioReview.objects.filter(number = number).exists():
            raise ValidationError(f'Порядковый номер не может повторяться. Номер {number} уже занят')
        return number


@admin.register(VideoReview)
class VideoReviewAdmin(admin.ModelAdmin):
    form = VideoReviewForm