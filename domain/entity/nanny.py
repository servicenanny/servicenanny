from dataclasses import dataclass
from datetime import datetime

from .worker_base import BaseWorkerRequired
from .type import WEEKDAYS


@dataclass
class Nanny(BaseWorkerRequired):
    created_at: datetime
    updated_at: datetime
    first_name: str
    last_name: str
    work_days: list[WEEKDAYS]
    age: int
    experience: int
    describe: str