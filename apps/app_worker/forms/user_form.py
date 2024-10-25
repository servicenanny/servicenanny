from django.forms import ModelForm
from django.contrib.auth import get_user_model


class UserForm(ModelForm):   
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']