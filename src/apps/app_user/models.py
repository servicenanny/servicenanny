from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    """
    Defines how the User(or the model to which attached)
    will create users and superusers.
    """

    def create_user(
        self,
        email, 
        password,
        **extra_fields
        ):
        """
        Create and save a user with the given email, password,
        and date_of_birth.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email) # lowercase the domain
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password) # hash raw password and set
        user.save()
        return user

    def create_superuser(
        self,
        email, 
        password,
        **extra_fields
        ):
        """
        Create and save a superuser with the given email and
        password. Extra fields are added
        to indicate that the user is staff, active, and indeed
        a superuser.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                _("Superuser must have is_staff=True.")
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                _("Superuser must have is_superuser=True.")
            )
        return self.create_user(
            email, 
            password, 
            **extra_fields
        )


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=255, verbose_name=_("Имя"), help_text=_("Введите имя"), null=True, blank = False)
    last_name = models.CharField(max_length=255, verbose_name=_("Фамилия"), help_text=_("Введите фамилию"), null=True, blank = False)
    age = models.PositiveSmallIntegerField(verbose_name=_("Возраст"), help_text=_("Введите ваш возраст"), null=True, blank = False)
    email = models.EmailField(verbose_name=_("Почта"), unique=True, null=True, blank = False)
    phone_number = PhoneNumberField(verbose_name="Номер телефона", unique=True, null=True, blank = False)
    is_verified = models.BooleanField(default=False, verbose_name=_("Верифицирован"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        unique_together = ('phone_number', 'email')