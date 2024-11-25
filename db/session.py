from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

from core.settings import settings


engine = create_engine(
    settings.DATABASE_URL, pool_size=10, max_overflow=20, pool_recycle=1800
)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
