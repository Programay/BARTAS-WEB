from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    f"postgresql://{config('POSTGRES_USER')}:{config('POSTGRES_PASSWORD')}@db:{config('POSTGRES_PORT')}/{config('POSTGRES_DB')}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
