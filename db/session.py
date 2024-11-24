
from sqlmodel import Field, Session, SQLModel, create_engine, select

from core.settings import  settings


engine = create_engine(settings.DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session

