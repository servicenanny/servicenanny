from dataclasses import dataclass
from typing import Protocol, TypeVar, Generic

from .base_repository import BaseRepository
from domain.entity import Nanny, User
from domain.entity.type import WEEKDAYS
from .user_subscribe_repository import UserSubscribeRepository


@dataclass
class UpdateNannyDTO:
    phone_number: str = None
    cost_per_hour: int = None
    photo: str = None
    work_days: list[WEEKDAYS] = None
    age: int = None
    experience: int = None
    describe: str = None

@dataclass
class AddNannyDTO:
    id: int
    user: User


class NannyRepository(BaseRepository[Nanny, AddNannyDTO, UpdateNannyDTO], Protocol):
    def get_fresh_subscriber_nanny(self, user_subscribe_repository: UserSubscribeRepository, *args, **kwargs):
        ...

    def get_fresh_subscriber_nanny_pagination(self, user_subscribe_repository: UserSubscribeRepository, count: int, *args, **kwargs):
        ...

    def is_have_nanny_permission(self, user: User) -> bool:
        ...