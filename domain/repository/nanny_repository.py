from dataclasses import dataclass
from typing import Protocol, TypeVar, Generic, Iterable

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


MNanny = TypeVar("MNanny")


class NannyRepository(BaseRepository[Nanny, AddNannyDTO, UpdateNannyDTO], Generic[MNanny], Protocol):
    def get_by_user_id(self, user_id: int, *args, **kwargs) -> Nanny:
        ...

    def is_nanny_exist(self, user_id: int, *args, **kwargs) -> bool:
        ...

    def get_fresh_subscriber_nanny(self, user_subscribe_repository: IUserSubscribeRepository, *args, **kwargs) -> Iterable[MNanny]:
        ...

    def get_fresh_subscriber_nanny_pagination(self, user_subscribe_repository: IUserSubscribeRepository, count: int, *args, **kwargs) -> Iterable[MNanny]:
        ...

    def get_fresh_subscriber_nannies_by_city(
            self, 
            user_subscribe_repository: IUserSubscribeRepository, 
            city_id: int, 
            *args, 
            **kwargs
        ) -> Iterable[MNanny]:
        ...

    def is_have_nanny_permission(self, user: User) -> bool:
        ...