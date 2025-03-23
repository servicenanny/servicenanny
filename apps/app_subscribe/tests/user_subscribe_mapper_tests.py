import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.app_subscribe.models import UserSubscribe
from apps.app_subscribe.repository.mapper import UserSubscribeMapper
from domain.repository.mapper import IMapper


class UserSubscribeMapperTest(TestCase):
    def __init__(self, methodName = "runTest", mapper: IMapper = UserSubscribeMapper()):
        self.mapper = mapper
        super().__init__(methodName)

    @pytest.mark.django_db
    def test_deep_to_domain(self):
        User = get_user_model()
        user = User(
            email = "test@mail.ru",
            password = "password",
            client_type = "N",
            is_superuser = False,
            is_staff = False
        )
        user.save()
        subscribe = UserSubscribe(
            user = user,
            subscribe_type = user.client_type
        )
        subscribe.save()
        result = self.mapper.deep_to_domain(subscribe)
        self.assertIsNotNone(result)