from contextlib import AbstractContextManager
from typing import Callable
from fastapi import APIRouter, Depends, status

from common.infrastructure.get_service import get_service
from user.create_user_dto import CreateUserDto
from sqlalchemy.orm import Session

from user.user import User

router = APIRouter(
    prefix='/users',
)


@router.get('/')
def get_users(session_factory: Callable[..., AbstractContextManager[Session]]):
    with session_factory() as session:
        return session.query(User).all()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: CreateUserDto, session_factory: Callable[..., AbstractContextManager[Session]]):
    user = User(
        name=request.name,
        email=request.email,
        phone_number=request.phone_number
    )

    with session_factory() as session:
        session.add(user)
        session.commit()
        session.refresh(user)

    return user
