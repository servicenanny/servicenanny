from dataclasses import dataclass
from datetime import datetime

from .user import User
from .type import CLIENT_TYPE


@dataclass
class Subscribe:
    id: int
    name: str
    short_description: str
    client_type: CLIENT_TYPE
    price: float
    day_range: int
    created_by: User
    created_at: datetime
    updated_at: datetime


    def __str__(self) -> str:
        return self.name