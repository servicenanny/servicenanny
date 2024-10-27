from dataclasses import dataclass

from .city import City


@dataclass
class User:
    id: int
    email: str
    password: str
    city: City = None
    is_superuser: bool = False
    is_curator: bool = False
    first_name: str = None
    last_name: str = None
