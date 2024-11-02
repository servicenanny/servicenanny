from domain.entity import User as DUser
from django.contrib.auth.models import AbstractBaseUser


def to_domain_user(user_model: AbstractBaseUser) -> DUser:
        return DUser(
            id = user_model.id,
            email = user_model.email,
            password = user_model.password,
            client_type = user_model.client_type,
            city = user_model.city,
            is_superuser = user_model.is_superuser,
            is_staff = user_model.is_staff
        )