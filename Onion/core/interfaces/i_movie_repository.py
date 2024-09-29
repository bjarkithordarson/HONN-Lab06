from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from typing import Callable, List
from sqlalchemy.orm import Session
from core.entities.movie import Movie

class IMovieRepository(ABC):
    @abstractmethod
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        pass

    @abstractmethod
    def get_all(self) -> List[Movie]:
        pass

    @abstractmethod
    def create_movie(self, movie: Movie) -> None:
        pass
