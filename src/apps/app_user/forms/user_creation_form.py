from django.contrib.auth.forms import UserCreationForm
from apps.app_user.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Specify the user model created while adding a user
    on the admin page.
    """
    class Meta:
        model = User
        fields = [
            "first_name", 
            "last_name",
            "age",
            "email",
            "password", 
            "is_staff",
            "is_active",
            "groups",
            "user_permissions"
        ]