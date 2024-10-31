from typing import Protocol, TypeVar, Generic, Iterable


T = TypeVar('T')
AddDto = TypeVar("AddDto")
UpdateDto = TypeVar("UpdateDto")

class BaseRepository(Protocol, Generic[T, AddDto, UpdateDto]):
    def add(self, dto: AddDto, *args, **kwargs) -> T:
        ...
    
    def get(self, *args, **kwargs) -> Iterable[T]:
        ...

    def get_by_id(self, id: int, *args, **kwargs) -> T:
        ...

    def update(self, dto: UpdateDto, *args, **kwargs) -> T:
        ...
    
    def delete(self, id: int, *args, **kwargs) -> None:
        ...