from dataclasses import dataclass
from typing import Protocol

from .base_repository import BaseRepository
from domain.entity.city import City


@dataclass
class AddDto:
    name: str

@dataclass
class UpadteDTO:
    name: str


class CityRepository(BaseRepository[City, AddDto, UpadteDTO], Protocol):
    ...
