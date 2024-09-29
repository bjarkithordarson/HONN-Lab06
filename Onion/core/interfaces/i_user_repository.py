from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from typing import Callable, List

from core.entities.user import User
from sqlalchemy.orm import Session


class IUserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def create_user(self, user: User) -> None:
        pass