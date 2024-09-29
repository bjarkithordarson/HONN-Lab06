from contextlib import AbstractContextManager
from typing import Callable
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from common.infrastructure.get_service import get_service
from pricing.create_pricing_dto import CreatePricingDto

from pricing.pricing import Pricing

router = APIRouter(
    prefix='/pricings',
)


@router.get('/')
def get_pricings(session_factory: Callable[..., AbstractContextManager[Session]]):
    with session_factory() as session:
        return session.query(Pricing).all()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_pricing(request: CreatePricingDto, session_factory: Callable[..., AbstractContextManager[Session]]):
    pricing = Pricing(
        name=request.name,
        price=request.price,
    )

    with session_factory() as session:
        session.add(pricing)
        session.commit()
        session.refresh(pricing)

    return pricing
