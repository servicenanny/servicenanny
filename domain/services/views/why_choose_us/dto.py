from dataclasses import dataclass
from typing import Iterable


@dataclass
class Reason:
    img: str
    title: Iterable[str]
    text: str


@dataclass
class WhyChooseUsBlock:
    title: Iterable[str]
    reasons: Iterable[Reason]