import logging

from django.http import HttpResponseServerError, HttpResponse
from django.views.generic import FormView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from domain.entity.type import CLIENT_TYPE
from domain.entity.user import User
from domain.port.api.payment import SuccessAPI
from apps.app_subscribe.forms import SuccessPaymentForm
from apps.app_subscribe.repository import UserSubscribeRepository
from apps.app_subscribe.services.success_payment import SuccessPaymentProcess
from apps.app_user.repository import UserRepository


logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name='dispatch')
class SuccessPaymentView(FormView, SuccessAPI):
    form_class = SuccessPaymentForm
    http_method_names = ['post']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = None
        self.process = SuccessPaymentProcess(
            UserRepository(),
            UserSubscribeRepository()
        )
    
    def post(self, request, *args, **kwargs):
        try:
            msg = self.process.verificate_prodamus(request)
            logger.info(f"Успешная верификация. Тело: {msg}")
            user_subscribe = self.process.create_user_subscribe(msg.get('customer_email'))
            logger.info(f"Успешно создана подписка: {str(user_subscribe)}")
            self.__set_user(user_subscribe.user)
            return HttpResponse("Success", status=200)
        except ValueError as e:
            logger.warning(f"Subscribe error. User: {request.user}. Error: {e}")
            return HttpResponseServerError(content="Ошибка сервера")
        except Exception as e:
            logger.fatal(str(e))
            return HttpResponseServerError(content="Ошибка сервера")
    
    def __set_user(self, user: User) -> None:
        self.user = user
    
    def get_success_url(self):
        if self.user.client_type == CLIENT_TYPE.NANNY:
            return reverse('nanny_profile')
        elif self.user.client_type == CLIENT_TYPE.PARENT:
            return reverse('nannies')
        raise ValueError(f"CLIENT_TYPE doesn't find. client_type is {self.user.client_type}")
