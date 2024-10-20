from typing import Any
from django.utils.translation import gettext as _
from django.db import models

WEEKDAYS = {
    '1': _(u'Понедельник'),
    '2': _(u'Вторник'),
    '3': _(u'Среда'),
    '4': _(u'Четверг'),
    '5': _(u'Пятница'),
    '6': _(u'Суббота'), 
    '7': _(u'Воскресенье'),
}


class WeekdayField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(WEEKDAYS.items()))
        kwargs['max_length'] = 7
        super(WeekdayField,self).__init__(*args, **kwargs)