from typing import Protocol, Generic, TypeVar


M = TypeVar('M')
E = TypeVar('E')


class IMapper(Generic[E, M]):
    def to_domain(self, model: M) -> E:
        """
        Map model to domain entity without get dependency field only get their id
        """
        ...

    def to_model(self, entity: E) -> M:
        """
        Map domain entity to model
        """
        ...

    def deep_to_domain(self, model: M) -> E:
        """
        Map model to domain entity with get dependency field
        """
        ...