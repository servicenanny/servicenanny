from dataclasses import dataclass

from .city import City
from .type import CLIENT_TYPE


@dataclass
class User:
    id: int
    email: str
    password: str
    client_type: CLIENT_TYPE
    city: City = None
    is_superuser: bool = False
    is_staff: bool = False

    def __str__(self):
        return self.email