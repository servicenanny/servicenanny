import math

from typing import Sized

from django import template


register = template.Library()


@register.filter
def rotation(arr: Sized, counter: int):
    result = math.ceil(((360 / len(arr) * (counter-1)) * -1)) - 3
    # if -45 < result or result <= -225:
    #     result -= 5
    # elif len(str(arr[counter-1])) > 15:
    #     result -= 5
    return result