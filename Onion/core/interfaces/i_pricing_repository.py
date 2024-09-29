from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from typing import Callable, List
from sqlalchemy.orm import Session
from core.entities.pricing import Pricing

class IPricingRepository(ABC):
    @abstractmethod
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        pass

    @abstractmethod
    def get_all(self) -> List[Pricing]:
        pass

    @abstractmethod
    def create_pricing(self, pricing: Pricing) -> None:
        pass
