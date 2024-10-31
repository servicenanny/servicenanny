from dataclasses import dataclass
from datetime import datetime

from .user import User


@dataclass
class UserSubscribe:
    id: int
    user: User
    created_at: datetime