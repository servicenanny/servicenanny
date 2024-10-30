from dataclasses import dataclass
from typing import Protocol, TypeVar, Generic

from apps.app_infrastructure.type.client_type import CLIENT_TYPE
from domain.entity.city import City

from .base_repository import BaseRepository
from domain.entity import User


@dataclass
class AddUserDTO:
    email: str
    password: str
    client_type: CLIENT_TYPE
    city: City = None
    is_superuser: bool = False
    is_staff: bool = False
    first_name: str = None
    last_name: str = None


@dataclass
class UpdateUserDTO:
    id: int
    email: str = None
    password: str = None
    client_type: CLIENT_TYPE = None
    city: City = None
    is_superuser: bool = False
    is_staff: bool = False
    first_name: str = None
    last_name: str = None


class UserRepository(Protocol, BaseRepository[User, AddUserDTO, UpdateUserDTO]):
    ...
