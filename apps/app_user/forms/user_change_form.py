from django.contrib.auth.forms import UserChangeForm
from apps.app_user.models import User


class CustomUserChangeForm(UserChangeForm):
    """
    Specify the user model edited while editing a user on the
    admin page.
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