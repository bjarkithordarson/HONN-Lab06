from contextlib import AbstractContextManager
from typing import Callable

from core.interfaces.i_user_repository import IUserRepository
from injector import inject

from core.entities.user import User
from sqlalchemy.orm import Session


class UserRepository(IUserRepository):
    @inject
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.__session_factory = session_factory

    def get_all(self) -> list[User]:
        with self.__session_factory() as session:
            return session.query(User).all()

    def create_user(self, user: User) -> None:
        with self.__session_factory() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
