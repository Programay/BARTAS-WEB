from decouple import config
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from .database import Base, get_db
from .main import app

engine = create_engine(
    "postgresql+psycopg2://testuser:testpassword@localhost/testdb",
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)
