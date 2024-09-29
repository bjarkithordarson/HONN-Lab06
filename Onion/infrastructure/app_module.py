from contextlib import AbstractContextManager
from typing import List, Callable

from injector import Binder, Module, provider, singleton, multiprovider
from sqlalchemy.orm import Session

from core.interfaces.i_movie_repository import IMovieRepository
from core.interfaces.i_pricing_repository import IPricingRepository
from core.interfaces.i_subscription_repository import ISubscriptionRepository
from core.interfaces.i_user_repository import IUserRepository
from database.database import Database
from database.mappings.mapping import Mapping
from database.mappings.movie_mapping import MovieMapping
from database.mappings.pricing_mapping import PricingMapping
from database.mappings.subscription_mapping import SubscriptionMapping
from database.mappings.user_mapping import UserMapping
from database.repositories.movie_repository import MovieRepository
from database.repositories.pricing_repository import PricingRepository
from database.repositories.subscription_repository import SubscriptionRepository
from database.repositories.user_repository import UserRepository
from infrastructure.settings import Settings


class AppModule(Module):
    def __init__(self, settings: Settings):
        self.__settings = settings

    @provider
    @singleton
    def provide_settings(self) -> Settings:
        return self.__settings

    @multiprovider
    @singleton
    def provide_mappings(self) -> List[Mapping]:
        # noinspection PyTypeChecker
        return [
            MovieMapping(),
            PricingMapping(),
            SubscriptionMapping(),
            UserMapping()
        ]

    @provider
    @singleton
    def provide_session_factory(self, database: Database) -> Callable[..., AbstractContextManager[Session]]:
        return database.session
    
    def configure(self, binder: Binder) -> None:
        binder.bind(IMovieRepository, to=MovieRepository)
        binder.bind(IPricingRepository, to=PricingRepository)
        binder.bind(ISubscriptionRepository, to=SubscriptionRepository)
        binder.bind(IUserRepository, to=UserRepository)