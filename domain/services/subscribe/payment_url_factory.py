from abc import ABC, abstractmethod

from domain.entity import User
from domain.entity.type import CLIENT_TYPE


class APaymentURLFactory(ABC):
    @abstractmethod
    def create_payment_url(self, user: User) -> str:
        ...

    @abstractmethod
    def get_cost(self, user: User) -> int:
        ...


class PaymentURLFactoryDirector:
    def __init__(self, nanny_factory: APaymentURLFactory, parent_factory: APaymentURLFactory):
        self.nanny_factory = nanny_factory
        self.parent_factory = parent_factory

    def get_link(self, user: User) -> str:
        if user.client_type == CLIENT_TYPE.NANNY:
            return self.nanny_factory.create_payment_url(user)
        elif user.client_type == CLIENT_TYPE.PARENT:
            return self.parent_factory.create_payment_url(user)
        raise ValueError(f"client type doesn't found. User {user.client_type}")
