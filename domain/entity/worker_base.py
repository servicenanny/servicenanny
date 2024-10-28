from dataclasses import dataclass

from .user import User


@dataclass
class BaseWorkerRequired:
    id: int
    user: User


@dataclass
class BaseWorkerDefaults:
    phone_number: str = None
    cost_per_hour: int = None
    photo: str = None