from .dto import PrizesSpinnerDTO


PRIZES_PARENT = (
    PrizesSpinnerDTO(
        text = "Скидка 100₽",
        color = "rgba(169, 209, 255, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 200₽",
        color = "rgba(217, 255, 154, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 300₽",
        color = "rgba(255, 213, 162, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 400₽",
        color = "rgba(255, 158, 223, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 500₽",
        color = "rgba(198, 161, 247, 1)",
        chance = 1,
        promo = 'PARENT'
    ),
    PrizesSpinnerDTO(
        text = "Обучение по самопрограм- мированию",
        color = "rgba(176, 242, 255, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Гайд от нейропсихолога",
        color = "rgba(255, 167, 167, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Книга от основателя сервиса",
        color = "rgba(255, 246, 142, 1)",
        chance = 0
    ),  
)

PRIZES_NANNY = (
    PrizesSpinnerDTO(
        text = "Скидка 50₽",
        color = "rgba(169, 209, 255, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 100₽",
        color = "rgba(217, 255, 154, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 200₽",
        color = "rgba(255, 213, 162, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 300₽",
        color = "rgba(255, 158, 223, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 400₽",
        color = "rgba(198, 161, 247, 1)",
        chance = 1
    ),
    PrizesSpinnerDTO(
        text = "Скидка 500₽",
        color = "rgba(255, 167, 167, 1)",
        chance = 0,
        promo = 'NANNY'
    ),
    PrizesSpinnerDTO(
        text = "Обучение по самопрограм- мированию",
        color = "rgba(176, 242, 255, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Гайд от нейропсихолог",
        color = "rgba(255, 246, 142, 1)",
        chance = 0
    ),
)


DISCOUNTS_PARENT = (100, 200, 400, 500)
DISCOUNTS_NANNY = (100, 200, 400, 600)