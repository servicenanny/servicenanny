from datetime import datetime
import logging
import copy

from django.http import HttpRequest, HttpResponseServerError, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse

from domain.entity.type import CLIENT_TYPE
from domain.entity import UserSubscribe, User
from domain.port.api.payment import SuccessAPI
from domain.repository.user_subscribe_repository import AddUserSubscribeDTO
from domain.repository.user_subscribe_repository import IUserSubscribeRepository as IUserSubscribeRepository
from domain.repository.user_repository import UserRepository as IUserRepository
from apps.app_subscribe.helper import ProdamusVerificate
from apps.app_subscribe.repository import UserSubscribeRepository
from apps.app_user.repository import UserRepository
from apps.app_user.utils import to_domain_user


logger = logging.getLogger(__name__)


class SuccessPaymentProcess(SuccessAPI):
    def __init__(
            self, 
            user_repository: IUserRepository, 
            user_subscribe_repository: IUserSubscribeRepository, 
            *args, 
            **kwargs
        ) -> None:
        super().__init__(*args, **kwargs)
        self.user = None
        self.payment_url: str = getattr(settings, "PAYMENT_URL")
        self.payment_secret_key: str = getattr(settings, "PAYMENT_SECRET_KEY")
        self._verificate = ProdamusVerificate(self.payment_secret_key)
        self.user_subscribe_repository = user_subscribe_repository
        self.user_repository = user_repository

    def verificate_prodamus(self, request: HttpRequest, *args, **kwargs) -> dict[str, str]:
        """
        Verify sign of payment and return body as dict
        """
        if not 'Sign' in request.headers:
            raise ValueError(f"Request is not valid")
        sign = request.headers.get('Sign')
        data = request.POST.dict()
        body_dict = copy.deepcopy(data)
        logger.info(f"Body dict {data}")
        is_verify = self._verificate.verify(data, sign)
        checkSign = self._verificate.sign(data, self.payment_secret_key)
        logger.info(checkSign)
        if not is_verify:
            raise ValueError(f"Request is not valid")
        body_dict = request.POST.dict()
        return body_dict
    
    def create_user_subscribe(self, user_email: str) -> UserSubscribe:
        """
        Create subscribe by user email and return subscribe
        """
        user = self.user_repository.get_by_email(user_email)
        dto = self.__get_add_user_subscribe_dto(user)
        return self.user_subscribe_repository.add(dto)
    
    def __get_add_user_subscribe_dto(self, user: User) -> AddUserSubscribeDTO:
        return AddUserSubscribeDTO(
            user = user,
            created_at = datetime.now()
        )
    
