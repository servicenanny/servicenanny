from django.contrib.auth import forms as auth_forms
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy
from django.contrib import admin

from .models import User

class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("email", "client_type", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password", "city")}),
        (gettext_lazy("Permissions"), {"fields": ("is_staff", "client_type", "is_superuser", "is_active", "groups")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide"),
                "fields": ("email", "password1", "password2"),
            },
        ),
        (gettext_lazy("Permissions"), {"fields": ("is_staff", "client_type", "is_superuser", "is_active", "groups")}),
    )
    list_filter = ('is_staff', "is_active", "is_superuser", "client_type")
    search_fields = ("email",)
    ordering = ("email",)