from django.http import HttpRequest
from django.urls import reverse

from apps.app_subscribe.repository import UserSubscribeRepository
from domain.services.subscribe import LeftoverDays, SUBSCRIBE_STATUS


def header_context_processor(request: HttpRequest):
    leftover_days = LeftoverDays()
    repository = UserSubscribeRepository()
    if not request.user.is_authenticated:
        return {
            'header_button_text': "Вход",
            'header_button_href': reverse('account_login')
        }
    header_button = leftover_days.get_subscribe_status(
        repository = repository, 
        user_id = request.user.id
    )
    if header_button == SUBSCRIBE_STATUS.NOT_AUTH:
        return {
            'header_button_text': "Вход",
            'header_button_href': reverse('account_login')
        }
    elif header_button == SUBSCRIBE_STATUS.NOT_ACTIVE_SUBSCRIBE:
        return {
            'header_button_text': "Подписаться",
            'header_button_href': reverse('home') + '#in_subscribe'
        }
    elif header_button == SUBSCRIBE_STATUS.ACTIVE_SUBSCRIBE:
        return {
            'end_range': leftover_days.get_leftover_days(repository, request.user.id).days
        }