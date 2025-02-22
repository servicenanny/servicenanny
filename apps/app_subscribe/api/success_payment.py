from datetime import datetime
import logging

from django.http import HttpResponseServerError
from django.views.generic import FormView
from django.urls import reverse

from domain.entity.type import CLIENT_TYPE
from domain.entity.user import User
from domain.port.api.payment import SuccessAPI
from domain.repository.user_subscribe_repository import IUserSubscribeRepository
from domain.repository.user_repository import UserRepository as IUserRepository
from apps.app_subscribe.forms import SuccessPaymentForm
from apps.app_subscribe.repository import UserSubscribeRepository
from apps.app_subscribe.services.success_payment import SuccessPaymentProcess
from apps.app_user.repository import UserRepository


logger = logging.getLogger(__name__)


class SuccessPaymentView(FormView, SuccessAPI):
    form_class = SuccessPaymentForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = None
        self.process = SuccessPaymentProcess(
            UserRepository(),
            UserSubscribeRepository()
        )
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        try:
            logger.info("Мы в post запросе")
            msg = self.process.verificate_prodamus(request)
            logger.info(msg)
            form = self.get_form()
            if form.is_valid():
                user_subscribe = self.process.create_user_subscribe(msg.get('customer_email'))
                self.__set_user(user_subscribe.user)
            else:
                return HttpResponseServerError(content="Invalid request")
        except ValueError as e:
            logger.warning(f"Subscribe error. User: {request.user}. Error: {e}")
            return HttpResponseServerError(content="Ошибка сервера")
        except Exception as e:
            logger.fatal(str(e))
            return HttpResponseServerError(content="Ошибка сервера")

    # def get(self, request, *args, **kwargs):
    #     try:
    #         msg = self.process.verificate_prodamus(request)
    #         logger.info(msg)
    #         user_subscribe = self.process.create_user_subscribe(msg.get('customer_email'))
    #         self.__set_user(user_subscribe.user)
    #         return HttpResponseRedirect(self._get_redirect_url())
    #     except ValueError as e:
    #         logger.warning(f"Subscribe error. User: {request.user}. Error: {e}")
    #         return HttpResponseServerError(content="Ошибка сервера")
    #     except Exception as e:
    #         logger.fatal(str(e))
    #         return HttpResponseServerError(content="Ошибка сервера")
    
    def __set_user(self, user: User) -> None:
        self.user = user
    
    def get_success_url(self):
        if self.user.client_type == CLIENT_TYPE.NANNY:
            return reverse('nanny_profile')
        elif self.user.client_type == CLIENT_TYPE.PARENT:
            return reverse('nannies')
        raise ValueError(f"CLIENT_TYPE doesn't find. client_type is {self.user.client_type}")
