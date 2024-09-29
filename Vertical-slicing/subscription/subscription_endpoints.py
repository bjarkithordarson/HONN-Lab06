from contextlib import AbstractContextManager
from fastapi import APIRouter, Depends, status

from common.infrastructure.get_service import get_service
from pricing.pricing import Pricing
from subscription.create_subscription_dto import CreateSubscriptionDto

from sqlalchemy.orm import Session, joinedload
from typing import Callable

from subscription.subscription import Subscription
from user.user import User

router = APIRouter(
    prefix='/subscriptions',
)


@router.get('/')
def get_users(session_factory: Callable[..., AbstractContextManager[Session]]):
    with session_factory() as session:
        return session.query(Subscription) \
            .options(joinedload(Subscription.pricing)) \
            .options(joinedload(Subscription.user)) \
            .all()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: CreateSubscriptionDto, session_factory: Callable[..., AbstractContextManager[Session]]):
    subscription = Subscription(
        start_date=request.start_date,
        end_date=request.end_date,
        user_id=request.user_id,
        pricing_id=request.pricing_id
    )

    with session_factory() as session:
        subscription.user = session.query(User).get(subscription.user_id)
        subscription.pricing = session.query(
            Pricing).get(subscription.pricing_id)
        session.add(subscription)
        session.commit()
        session.refresh(subscription.user)
        session.refresh(subscription.pricing)

    return subscription
