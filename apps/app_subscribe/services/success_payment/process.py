from datetime import datetime
import logging
import copy
import re
import hashlib

from django.http import HttpRequest
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

from domain.entity import UserSubscribe, User
from domain.port.api.payment import SuccessAPI
from domain.repository.user_subscribe_repository import AddUserSubscribeDTO
from domain.repository.user_subscribe_repository import IUserSubscribeRepository as IUserSubscribeRepository
from domain.repository.user_repository import UserRepository as IUserRepository
from apps.app_subscribe.helper import ProdamusVerificate


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
        data = self.__parse_post(request)
        body_dict = copy.deepcopy(data)
        is_verify = self._verificate.verify(data, sign)
        if not is_verify:
            logger.info(f"Expected result: {sign}, created: {self._verificate.sign(data)}")
            raise ValueError(f"Request is not valid")
        return body_dict
    
    def __parse_post(self, request: HttpRequest) -> dict[str, str]:
        data = {
            'date': request.POST.get('date'),
            'order_id': request.POST.get('order_id'),
            'order_num': request.POST.get('order_num'),
            'domain': request.POST.get('domain'),
            'sum': request.POST.get('sum'),
            'currency': request.POST.get('currency'),
            'customer_phone': request.POST.get('customer_phone'),
            'customer_email': request.POST.get('customer_email'),
            'customer_extra': request.POST.get('customer_extra'),
            'payment_type': request.POST.get('payment_type'),
            'commission': request.POST.get('commission'),
            'commission_sum': request.POST.get('commission_sum'),
            'attempt': request.POST.get('attempt'),
            'sys': request.POST.get('sys'),
            'payment_status': request.POST.get('payment_status'),
            'payment_status_description': request.POST.get('payment_status_description'),
            'payment_init': request.POST.get('payment_init')
        }
        products = []
        pattern = re.compile(r'products\[(\d+)\]\[(\w+)\]')
        for key in request.POST.keys():
            match = pattern.match(key)
            if match:
                index, field = match.groups()
                index = int(index)
                # Убедимся, что список products достаточно большой
                while len(products) <= index:
                    products.append({})
                products[index][field] = request.POST.get(key)
        data['products'] = products
        return data
    
    def create_user_subscribe(self, user_email: str, client_type: str) -> UserSubscribe:
        """
        Create subscribe by user email and return subscribe
        """
        try:
            password = get_random_string(10)
            user = User.objects.create_user(
                email=user_email,
                client_type=client_type
            )
            user.set_password(password)
            user.save()

            user = self.user_repository.get_by_email(user_email)
            logger.info(f"[create_user_subscribe | user]: {str(user)}")
            dto = self.__get_add_user_subscribe_dto(user)
            logger.info(f"[create_user_subscribe | dto]: {dto}")
            result = self.user_subscribe_repository.add(dto)
            logger.info(f"[create_user_subscribe | result]: {result}")

            send_mail(
                'Ваш доступ к сервису',
                f'Ваш логин: {user_email}\nПароль: {password}\nТип аккаунта: {client_type}',
                'noreply@yourdomain.com',
                [user_email]
            )
            return result
        except Exception as e:
            logger.error(str(e))
            raise e
    
    def __get_add_user_subscribe_dto(self, user: User) -> AddUserSubscribeDTO:
        return AddUserSubscribeDTO(
            user = user,
            created_at = datetime.now()
        )
    
