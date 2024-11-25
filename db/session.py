from sqlmodel import Field, Session, SQLModel, create_engine, select

from core.settings import settings


engine = create_engine(
    settings.DATABASE_URL, pool_size=10, max_overflow=20, pool_recycle=1800
)


def get_session():
    with Session(engine) as session:
        yield session
