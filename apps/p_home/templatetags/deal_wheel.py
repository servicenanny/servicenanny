import math

from typing import Sized

from django import template


register = template.Library()


@register.filter
def rotation(arr: Sized, counter: int):
    return math.trunc(((360 / len(arr) * (counter-1)) * -1) - 180 / len(arr))