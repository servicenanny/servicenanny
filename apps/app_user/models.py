# from django.db.models import EmailField
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import BaseUserManager
# from multiselectfield import MultiSelectField
# from django.utils.translation import gettext_lazy as _

# from apps.app_infrastructure.type import CLIENT_TYPE


# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
#     def create_user(self, email, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError(_('The Email must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self.create_user(email, password, **extra_fields)


# class User(AbstractUser):
#     workers = MultiSelectField(
#         choices = CLIENT_TYPE.get_choices(),
#         default = CLIENT_TYPE.PARENT.value[0],
#         verbose_name = _("Тип пользователя"),
#         help_text = _("Выберите тип пользователя")
#     )
#     email = EmailField(_('email address'), unique=True)

#     username = None

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self) -> str:
#         return self.email