from dataclasses import dataclass
from typing import Protocol, TypeVar, Generic

from .base_repository import BaseRepository
from domain.entity import Nanny, User
from domain.entity.type import WEEKDAYS
from .user_subscribe_repository import IUserSubscribeRepository


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
    user_id: int


class NannyRepository(BaseRepository[Nanny, AddNannyDTO, UpdateNannyDTO], Protocol):
    def get_by_user_id(self, user_id: int, *args, **kwargs) -> Nanny:
        ...

    def is_nanny_exist(self, user_id: int, *args, **kwargs) -> bool:
        ...

    def get_fresh_subscriber_nanny(self, user_subscribe_repository: IUserSubscribeRepository, *args, **kwargs):
        ...

    def get_fresh_subscriber_nanny_pagination(self, user_subscribe_repository: IUserSubscribeRepository, count: int, *args, **kwargs):
        ...

    def is_have_nanny_permission(self, user: User) -> bool:
        ...