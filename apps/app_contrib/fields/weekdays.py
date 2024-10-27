from typing import Any
from django.utils.translation import gettext as _
from django.db import models

WEEKDAYS = {
    '1': _(u'Пн'),
    '2': _(u'Вт'),
    '3': _(u'Ср'),
    '4': _(u'Чт'),
    '5': _(u'Пт'),
    '6': _(u'Сб'), 
    '7': _(u'Вс'),
}


class WeekdayField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(WEEKDAYS.items()))
        kwargs['max_length'] = 7
        super(WeekdayField,self).__init__(*args, **kwargs)