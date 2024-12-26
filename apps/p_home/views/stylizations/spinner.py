from typing import Sized

from domain.services.prizes.dto import PrizesSpinnerDTO


class SpinnerStylization:
    def get_conic_gradient(self, prizes: list[PrizesSpinnerDTO]) -> str:
        style = 'conic-gradient(from -25deg, '
        count = len(prizes)
        for i in range(count-1, 0, -1):
            degree = str(self.__deal_wheel_degree(count, i)).replace(',', '.')
            style += f'{prizes[i].color} 0 {degree}%, '
        style += f'{prizes[0].color} 0 {self.__deal_wheel_degree(count, 0)}%)'
        return style

    def __deal_wheel_degree(self, arr_len: int, counter: int) -> float:
        return (100 / arr_len) * (arr_len - counter)