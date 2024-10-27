from typing import Protocol, TypeVar, Generic


T = TypeVar('T')
AddDto = TypeVar("AddDto")
UpdateDto = TypeVar("UpdateDto")

class BaseRepository(Protocol, Generic[T, AddDto, UpdateDto]):
    def add(self, dto: AddDto, *args, **kwargs) -> T:
        ...
    
    def get(self, *args, **kwargs) -> T:
        ...

    def update(self, dto: AddDto, *args, **kwargs) -> T:
        ...
    
    def delete(self, dto: UpdateDto, *args, **kwargs) -> None:
        ...