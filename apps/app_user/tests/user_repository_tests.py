from django.test import TestCase
import pytest

from apps.app_user.repository import UserRepository
from domain.repository.user_repository import AddUserDTO


class UserRepositoryTest(TestCase):
    def __init__(self, methodName = "runTest"):
        self.repository = UserRepository()
        super().__init__(methodName)

    @pytest.mark.django_db
    def test_add_none(self):
        dto = AddUserDTO(
            email = "test@mail.ru",
            password = "password",
            client_type = "N",
            is_superuser = False,
            is_staff = False
        )
        result = self.repository.add(dto)
        self.assertIsNotNone(result)

    @pytest.mark.django_db
    def test_add_to_model(self):
        dto = AddUserDTO(
            email = "test@mail.ru",
            password = "password",
            client_type = "N",
            is_superuser = False,
            is_staff = False
        )
        entity = self.repository.add(dto)
        dto = AddUserDTO(
            email = "test2@mail.ru",
            password = entity.password,
            client_type = entity.client_type,
            is_superuser = entity.is_superuser,
            is_staff = entity.is_staff
        )
        result = self.repository.add(dto)
        self.assertEqual(result.password, entity.password)
        self.assertEqual(result.client_type, entity.client_type)
        
    def test_str_method(self):
        self.assertEqual("Test", "Test")
