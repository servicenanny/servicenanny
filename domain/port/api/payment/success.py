from typing import Protocol

from domain.repository.user_subscribe_repository import IUserSubscribeRepository, AddUserSubscribeDTO


class SuccessAPI(Protocol):
    def create_user_subscribe(self, repository: IUserSubscribeRepository, dto: AddUserSubscribeDTO, *args, **kwargs):
        ...