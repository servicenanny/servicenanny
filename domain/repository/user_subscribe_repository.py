from dataclasses import dataclass
from datetime import timedelta
from typing import Protocol

from .base_repository import BaseRepository
from domain.entity import City, User


@dataclass
class UpdateUserSubscribeDTO:
    name: str

@dataclass
class AddUserSubscribeDTO:
    name: str


class UserSubscribeRepository(BaseRepository[City, AddUserSubscribeDTO, UpdateUserSubscribeDTO], Protocol):
    def get_leftover_days(self, user_id: int, *args, **kwargs) -> timedelta | None:
        ...

    def get_fresh_subscriber(self) -> list[int]:
        ...

    def is_have_subscribe_permission(self, user: User) -> bool:
        ...