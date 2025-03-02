from enum import Enum


class CLIENT_TYPE(Enum):
    NANNY = ('N', 'Няни')
    PARENT = ('P', 'Родители')

    @classmethod
    def get_choices(cls):
        return [(status.value[0], status.value[1]) for status in cls]
    
    def __eq__(self, value: object) -> bool:
        return self.value[0] == value

    @classmethod
    def from_value(cls, value: str):
        """
        Возвращает объект enum по символу.
        """
        for member in cls:
            if member.value[0] == value:
                return member
        raise ValueError(f"Нет члена enum с значением {value}")