from typing import Protocol


class FailureAPI(Protocol):
    def get(*args, **kwargs):
        ...