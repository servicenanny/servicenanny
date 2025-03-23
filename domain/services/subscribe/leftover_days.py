from enum import Enum
from datetime import timedelta

from domain.repository import IUserSubscribeRepository


class SUBSCRIBE_STATUS(Enum):
    NOT_AUTH = ('NA', 'Вход')
    NOT_ACTIVE_SUBSCRIBE = ('NS', 'Подписаться')
    ACTIVE_SUBSCRIBE = ('AS', 'Осталось дней')

    @classmethod
    def get_choices(cls):
        return [(status.value[0], status.value[1]) for status in cls]
    
    def __eq__(self, value: object) -> bool:
        return self.value[0] == value


class LeftoverDays:
    def __init__(self):
        self.leftover_days = None

    def get_subscribe_status(self, repository: IUserSubscribeRepository, user_id: int):
        if self.leftover_days is None:
            self.leftover_days = repository.get_leftover_days(user_id)
        if self.leftover_days is None or self.leftover_days <= timedelta():
            return SUBSCRIBE_STATUS.NOT_ACTIVE_SUBSCRIBE
        else:
            return SUBSCRIBE_STATUS.ACTIVE_SUBSCRIBE
        
    def get_leftover_days(self, repository: IUserSubscribeRepository, user_id: int) -> timedelta:
        if self.leftover_days is None: 
            self.leftover_days = repository.get_leftover_days(user_id)
        return self.leftover_days