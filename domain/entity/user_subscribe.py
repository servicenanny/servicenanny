from dataclasses import dataclass
from datetime import datetime
from typing import Literal

from .user import User
from domain.entity.type import CLIENT_TYPE


@dataclass
class UserSubscribe:
    id: int
    created_at: datetime
    user_id: int
    subscribe_type: Literal[CLIENT_TYPE.NANNY, CLIENT_TYPE.PARENT]
    user: User | None = None


    def __str__(self):
        return f"[{self.created_at}] user: {self.user_id}"