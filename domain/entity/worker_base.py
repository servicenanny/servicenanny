from dataclasses import dataclass

from .user import User


@dataclass
class BaseWorkerRequired:
    id: int
    user: User
    phone_number: str
    cost_per_hour: str
    photo: str