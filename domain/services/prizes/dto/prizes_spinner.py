from dataclasses import dataclass


@dataclass
class PrizesSpinnerDTO:
    text: str
    color: str
    chance: int
    promo: str | None = None

    def __eq__(self, value):
        self.text == value.text

    def __str__(self):
        return self.text