from typing import Iterable

from .dto import PrizesSpinnerDTO
from .const import PRIZES_NANNY, PRIZES_PARENT
from domain.entity.type.client_type import CLIENT_TYPE


class PrizesSpinner:
    def get_client_context(self, client_type: CLIENT_TYPE) -> Iterable[PrizesSpinnerDTO]:
        """
        Return iter of PrizesSpinnerDTO by client choose type
        """
        if client_type == CLIENT_TYPE.NANNY:
            return PRIZES_NANNY
        elif client_type ==  CLIENT_TYPE.PARENT:
            return PRIZES_PARENT
        else:
            raise ValueError(f'This type is not implemented {client_type}')