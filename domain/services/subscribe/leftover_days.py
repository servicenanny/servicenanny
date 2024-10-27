from enum import Enum
from datetime import timedelta

from domain.repository import UserSubscribeRepository


class BUTTON_STATUS(Enum):
    NOT_AUTH = ('NA', 'Вход')
    NOT_ACTIVE_SUBSCRIBE = ('NS', 'Подписаться')
    ACTIVE_SUBSCRIBE = ('AS', 'Осталось дней')

    @classmethod
    def get_choices(cls):
        return [(status.value[0], status.value[1]) for status in cls]
    
    def __eq__(self, value: object) -> bool:
        return self.value[0] == value


class LeftoverDays:
    def get_subscribe_button_text(self, repository: UserSubscribeRepository, user_id: int) -> str:
        leftover_days = repository.get_leftover_days(user_id)
        if leftover_days is None:
            return BUTTON_STATUS.NOT_AUTH.value[1]
        elif leftover_days <= timedelta():
            return BUTTON_STATUS.NOT_ACTIVE_SUBSCRIBE.value[1]
        else:
            return BUTTON_STATUS.ACTIVE_SUBSCRIBE.value[1] + " " + str(leftover_days.days)