from enum import Enum


class WEEKDAYS(Enum):
    MONDAY = ('0', 'Пн')
    TUESDAY = ('1', 'Вт')
    WEDNESDAY = ('2', 'Ср')
    THURSDAY = ('3', 'Чт')
    FRIDAY = ('4', 'Пт')
    SATURDAY = ('', 'Сб')
    SUNDAY = ('6', 'Вс')

    @classmethod
    def get_choices(cls):
        return [(status.value[0], status.value[1]) for status in cls]
    
    def __eq__(self, value: object) -> bool:
        return self.value[0] == value
