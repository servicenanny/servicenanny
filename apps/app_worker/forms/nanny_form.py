from django.forms import ModelForm, Textarea

from apps.app_worker.models import Nanny


class NannyForm(ModelForm):   
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Nanny
        fields = ['phone_number', 'age', 'experience', 'cost_per_hour', 'describe', 'skills', 'work_days']
        widgets = {
            'describe': Textarea(attrs={'cols': 60, 'rows': 30}),
            'skills': Textarea(attrs={'cols': 60, 'rows': 20}),
        }