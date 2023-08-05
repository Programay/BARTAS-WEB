from uuid import uuid4

from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID

from ..database import Base


class User(Base):
    __tablename__ = "users"

    uuid = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    table = Column(String)
