from typing import Protocol

from domain.repository.user_subscribe_repository import UserSubscribeRepository, AddUserSubscribeDTO


class SuccessAPI(Protocol):
    def create_user_subscribe(self, repository: UserSubscribeRepository, dto: AddUserSubscribeDTO, *args, **kwargs):
        ...