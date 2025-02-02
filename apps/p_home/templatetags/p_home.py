import math

from typing import Sized

from django import template


register = template.Library()


@register.filter
def rotation(arr: Sized, counter: int):
    result = math.ceil(((360 / len(arr) * (counter-1)) * -1)) - 3
    return result


@register.filter
def int_divide(value: int, divisor: int) -> int:
    try:
        return int(value) // int(divisor)
    except (ValueError, ZeroDivisionError):
        return 0