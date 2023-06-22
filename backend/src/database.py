from datetime import datetime

from decouple import config
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped

engine = create_engine(
    f"postgresql://{config('POSTGRES_USER')}:{config('POSTGRES_PASSWORD')}@db:{config('POSTGRES_PORT')}/{config('POSTGRES_DB')}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    date_creation: Mapped[datetime] = mapped_column(server_default=func.now())
    date_modified: Mapped[datetime] = mapped_column(onupdate=func.now())


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
