from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from typing import Callable, List

from injector import inject
from sqlalchemy.orm import Session, joinedload
from core.entities.pricing import Pricing
from core.entities.subscription import Subscription
from core.entities.user import User


class ISubscriptionRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Subscription]:
        pass

    @abstractmethod
    def create_subscription(self, subscription: Subscription) -> None:
        pass