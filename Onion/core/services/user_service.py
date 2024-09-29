from injector import inject

from core.interfaces.i_user_repository import IUserRepository
from core.entities.user import User


class UserService:
    @inject
    def __init__(self, repository: IUserRepository):
        self.__repository = repository

    def get_all(self) -> list[User]:
        return self.__repository.get_all()

    def create_user(self, user: User):
        self.__repository.create_user(user)
