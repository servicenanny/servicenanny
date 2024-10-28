from dataclasses import dataclass
from datetime import datetime

from .worker_base import BaseWorkerDefaults, BaseWorkerRequired
from .type import WEEKDAYS


@dataclass
class NannyRequired(BaseWorkerRequired):
    created_at: datetime
    updated_at: datetime
    

@dataclass
class NannyDefaults(BaseWorkerDefaults):
    work_days: list[WEEKDAYS] = None
    age: int = None
    experience: int = None
    describe: str = None


@dataclass
class Nanny(NannyDefaults, NannyRequired):
    ...