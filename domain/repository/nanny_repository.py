from dataclasses import dataclass
from typing import Protocol, TypeVar, Generic

from .base_repository import BaseRepository
from domain.entity import Nanny
from .user_subscribe_repository import UserSubscribeRepository


@dataclass
class UpdateNannyDTO:
    name: str

@dataclass
class AddNannyDTO:
    name: str


class NannyRepository(BaseRepository[Nanny, AddNannyDTO, UpdateNannyDTO], Protocol):
    def get_fresh_subscriber_nanny(self, user_subscribe_repository: UserSubscribeRepository, *args, **kwargs):
        ...