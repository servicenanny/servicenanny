from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Protocol, Iterable

from .base_repository import BaseRepository
from domain.entity.type import CLIENT_TYPE
from domain.entity import UserSubscribe, User


@dataclass
class AddUserSubscribeDTO:
    user: User
    created_at: datetime

@dataclass
class UpdateUserSubscribeDTO:
    id: int
    user: User | None = None
    created_at: datetime | None = None


class IUserSubscribeRepository(BaseRepository[UserSubscribe, AddUserSubscribeDTO, UpdateUserSubscribeDTO], Protocol):
    def get_leftover_days(self, user_id: int, *args, **kwargs) -> timedelta | None:
        ...

    def get_fresh_subscriber(self, *args, **kwargs) -> Iterable[int]:
        ...

    def get_fresh_subscriber_by_type(self, client_type: CLIENT_TYPE, *args, **kwargs) -> Iterable[int]:
        ...

    def filter_subscriber_by_type(self, user_subscribers: Iterable[UserSubscribe], client_type: CLIENT_TYPE, *args, **kwargs) -> Iterable[UserSubscribe]:
        ...

    def is_have_subscribe_permission(self, user: User, client_type: CLIENT_TYPE, *args, **kwargs) -> bool:
        ...