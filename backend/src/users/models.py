from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import Boolean, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    # For IDE type checking only
    from src.orders.models import BarOrder


class User(Base):
    __tablename__ = "users"

    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid4
    )
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str | None] = mapped_column(
        String, unique=True, index=True, nullable=True
    )
    password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False)
    table: Mapped[str | None]

    # Relations
    bar_orders: Mapped[list["BarOrder"]] = relationship(
        "BarOrder", back_populates="user"
    )
