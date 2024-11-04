from datetime import datetime
import logging

from django.http import HttpRequest, HttpResponseServerError, HttpResponseRedirect
from django.views.generic import RedirectView
from django.conf import settings
from django.urls import reverse

from domain.entity.type import CLIENT_TYPE
from domain.port.api.payment import SuccessAPI
from domain.repository.user_subscribe_repository import AddUserSubscribeDTO
from domain.repository.user_subscribe_repository import UserSubscribeRepository as IUserSubscribeRepository
from domain.repository.user_repository import UserRepository as IUserRepository
from apps.app_subscribe.helper import ProdamusVerificate
from apps.app_subscribe.repository import UserSubscribeRepository
from apps.app_user.repository import UserRepository
from apps.app_user.utils import to_domain_user


logger = logging.getLogger(__name__)


class SuccessPaymentView(RedirectView, SuccessAPI):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = None
        self.verificate = ProdamusVerificate()
        self.payment_url = getattr(settings, "PAYMENT_URL")
        self.payment_secret_key = getattr(settings, "PAYMENT_SECRET_KEY")
        print(self.payment_secret_key)
        self.user_subscribe_repository: IUserSubscribeRepository = UserSubscribeRepository()
        self.user_repository: IUserRepository = UserRepository()

    def post(self, request, *args, **kwargs):
        try:
            msg = self._verificate_prodamus(request)
            self.__set_user(msg.get('customer_email'))
            dto = self.__get_add_user_subscribe_dto()
            self.create_user_subscribe(self.user_subscribe_repository, dto)
            return HttpResponseRedirect(self._get_redirect_url())
        except ValueError as e:
            logger.warning(f"Subscribe error. User: {request.user}. Error: {e}")
            return HttpResponseServerError(content="Ошибка сервера")
        except Exception as e:
            logger.fatal(str(e))
            return HttpResponseServerError(content="Ошибка сервера")
    
    def _verificate_prodamus(self, request: HttpRequest) -> dict[str, str]:
        if 'Sign' in request.headers:
            raise ValueError(f"Request is not valid")
        elif sign := request.headers.get('Sign') is None:
            raise ValueError("Needed param is None")
        logger.info(f"Header sign {sign}")
        body_dict = self.verificate.parse(request.body)
        check_sign = self.verificate.sign(body_dict, self.payment_secret_key)
        logger.info(f"Our sign {check_sign}")
        logger.info(f"Body dict {body_dict}")
        verify_result = self.verificate.verify(body_dict, sign, self.payment_secret_key)
        if verify_result == False: raise ValueError("Payment message is not verify")
        return body_dict
    
    def __set_user(self, email: str) -> None:
        self.user = self.user_repository.get_by_email(email)
    
    def __get_add_user_subscribe_dto(self) -> AddUserSubscribeDTO:
        return AddUserSubscribeDTO(
            user = to_domain_user(self.user),
            created_at = datetime.now()
        )
  
    def create_user_subscribe(self, repository, dto, *args, **kwargs):
        return repository.add(dto)
    
    def _get_redirect_url(self, *args, **kwargs):
        if self.user.client_type == CLIENT_TYPE.NANNY:
            return reverse('nanny_profile')
        elif self.user.client_type == CLIENT_TYPE.PARENT:
            return reverse('nannies')
        raise ValueError(f"CLIENT_TYPE doesn't find. client_type is {self.user.client_type}")
    
