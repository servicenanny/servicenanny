from enum import Enum


class CLIENT_TYPE(Enum):
    NANNY = ('N', 'Няни')
    PARENT = ('P', 'Родители')

    @classmethod
    def get_choices(cls):
        return [(status.value[0], status.value[1]) for status in cls]
    
    def __eq__(self, value: object) -> bool:
        return self.value[0] == value
