from datetime import datetime

import pytest
from django.test import TestCase

from apps.app_subscribe.repository import UserSubscribeRepository
from apps.app_user.repository import UserRepository
from domain.repository.user_subscribe_repository import AddUserSubscribeDTO
from domain.repository.user_repository import AddUserDTO
from domain.repository import UserRepository as IUserRepository
from domain.repository import IUserSubscribeRepository


class UserSubscribeRepositoryTest(TestCase):
    def __init__(
            self, 
            methodName = "runTest", 
            subscribe_repository: IUserSubscribeRepository = UserSubscribeRepository(),
            user_repository: IUserRepository = UserRepository()
        ):
        self.subscribe_repository = subscribe_repository
        self.user_repository = user_repository
        super().__init__(methodName)

    @pytest.mark.django_db
    def test_add(self):
        add_user_dto = AddUserDTO(
            email = "test@mail.ru",
            password = "password",
            client_type = "N",
            is_superuser = False,
            is_staff = False
        )
        user = self.user_repository.add(add_user_dto)
        dto = AddUserSubscribeDTO(
            user = user,
            created_at = datetime.now()
        )
        result = self.subscribe_repository.add(dto)
        self.assertIsNotNone(result)
