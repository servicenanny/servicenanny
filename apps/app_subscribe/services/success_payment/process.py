from datetime import datetime
import logging

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
        self._verificate = ProdamusVerificate()
        self.payment_url = getattr(settings, "PAYMENT_URL")
        self.payment_secret_key = getattr(settings, "PAYMENT_SECRET_KEY")
        self.user_subscribe_repository = user_subscribe_repository
        self.user_repository = user_repository

    def verificate_prodamus(self, request: HttpRequest, *args, **kwargs) -> dict[str, str]:
        """
        Verify sign of payment and return body as dict
        """
        logger.info(request.method)
        logger.info(request.headers)
        if not 'Sign' in request.headers:
            raise ValueError(f"Request is not valid")
        sign = request.headers.get('Sign')
        logger.info(f"Header sign {sign}")
        body_dict = self._verificate.parse(request.body)
        check_sign = self._verificate.sign(body_dict, self.payment_secret_key)
        logger.info(f"Our sign {check_sign}")
        logger.info(f"Body dict {body_dict}")
        verify_result = self._verificate.verify(body_dict, sign, self.payment_secret_key)
        if verify_result == False: raise ValueError("Payment message is not verify")
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
    
