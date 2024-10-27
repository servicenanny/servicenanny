from dataclasses import dataclass
from datetime import datetime

from .subscribe import Subscribe
from .user import User


@dataclass
class UserSubscribe:
    id: int
    user: User
    subscribe: Subscribe
    created_at: datetime