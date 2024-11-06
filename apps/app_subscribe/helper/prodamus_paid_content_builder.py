from django.urls import reverse

from domain.entity.type import CLIENT_TYPE
from domain.const.subscribe import SUBSCRIBE_NANNY_COST, SUBSCRIBE_NANNY_NAME, SUBSCRIBE_PARENT_COST, SUBSCRIBE_PARENT_NAME
from domain.const.courses import NANNY_COURSE_LINK


class ProdamusPaidContentBuilder:
    def build(self, client_type: CLIENT_TYPE):
        if client_type == CLIENT_TYPE.NANNY:
            return self.__get_nanny_paid_text()
        elif client_type == CLIENT_TYPE.PARENT:
            return self.__get_parent_paid_text()
        elif client_type is None:
            return None
        raise ValueError(f"client_type must be CLIENT_TYPE. Value {client_type}")
    
    def __get_nanny_paid_text(self) -> str:
        return f"""
                Спасибо за покупку \"{SUBSCRIBE_NANNY_NAME}\" за {SUBSCRIBE_NANNY_COST} рублей. Вы успешно добавлены в базу нянь.
                По ссылке вам доступны материалы для обучения: {NANNY_COURSE_LINK}
                """
    
    def __get_parent_paid_text(self) -> str:
        return f"Спасибо за покупку \"{SUBSCRIBE_PARENT_NAME}\" за {SUBSCRIBE_PARENT_COST} рублей. Вам открыт доступ к базе нянь по ссылке {reverse('nannies')}"
