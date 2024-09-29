from injector import inject

from core.interfaces.i_pricing_repository import IPricingRepository
from core.entities.pricing import Pricing


class PricingService:
    @inject
    def __init__(self, repository: IPricingRepository) -> None:
        self.__repository = repository

    def get_all(self) -> list[Pricing]:
        return self.__repository.get_all()

    def create_pricing(self, pricing: Pricing) -> None:
        self.__repository.create_pricing(pricing)
