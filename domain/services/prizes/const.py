from .dto import PrizesSpinnerDTO


PRIZES_PARENT = (
    PrizesSpinnerDTO(
        text = "Скидка 100₽",
        color = "rgba(254, 233, 106, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 200₽",
        color = "rgba(96, 175, 27, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 300₽",
        color = "rgba(255, 213, 162, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 400₽",
        color = "rgba(189, 43, 35, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 500₽",
        color = "rgba(249, 195, 64, 1)",
        chance = 1,
        promo = 'PARENT'
    ),
    PrizesSpinnerDTO(
        text = "Обучение по самопрограм- мированию",
        color = "rgba(218, 224, 224, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Гайд от нейропсихолога",
        color = "rgba(255, 159, 110, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Книга от основателя сервиса",
        color = "rgba(166, 213, 254, 1)",
        chance = 0
    ),  
)

PRIZES_NANNY = (
    PrizesSpinnerDTO(
        text = "Скидка 50₽",
        color = "rgba(254, 233, 106, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Скидка 100₽",
        color = "rgba(96, 175, 27, 1)",
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
        color = "rgba(189, 43, 35, 1)",
        chance = 1
    ),
    PrizesSpinnerDTO(
        text = "Скидка 500₽",
        color = "rgba(249, 195, 64, 1)",
        chance = 0,
        promo = 'NANNY'
    ),
    PrizesSpinnerDTO(
        text = "Обучение по самопрограм- мированию",
        color = "rgba(218, 224, 224, 1)",
        chance = 0
    ),
    PrizesSpinnerDTO(
        text = "Гайд от нейропсихолог",
        color = "rgba(255, 159, 110, 1)",
        chance = 0
    ),
)


DISCOUNTS_PARENT = (100, 200, 400, 500)
DISCOUNTS_NANNY = (100, 200, 400, 600)