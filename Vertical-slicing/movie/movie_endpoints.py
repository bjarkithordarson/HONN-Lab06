from contextlib import AbstractContextManager
from typing import Callable
from fastapi import APIRouter, Depends, status
from movie.create_movie_dto import CreateMovieDto
from common.infrastructure.get_service import get_service
from sqlalchemy.orm import Session

from movie.movie import Movie

router = APIRouter(
    prefix='/movies',
)


@router.get('/')
def get_movies(session_factory: Callable[..., AbstractContextManager[Session]]):
    with session_factory() as session:
            return session.query(Movie).all()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_movie(request: CreateMovieDto, session_factory: Callable[..., AbstractContextManager[Session]]):
    movie = Movie(
        name=request.name,
        description=request.description,
        imdb_url=request.imdb_url,
    )

    with session_factory() as session:
            session.add(movie)
            session.commit()
            session.refresh(movie)

    return movie
