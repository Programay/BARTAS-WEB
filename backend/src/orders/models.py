from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import Enum, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database import Base
from backend.src.orders import constants

if TYPE_CHECKING:
    # For IDE type checking only
    from backend.src.drinks.models import Drink
    from backend.src.storage.models import IngredientStorage
    from backend.src.users.models import User


class BarOrder(Base):
    __tablename__ = "bar_orders"

    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid4
    )

    status: Mapped[constants.OrderStatus] = mapped_column(
        Enum(constants.OrderStatus),
        nullable=False,
        default=constants.OrderStatus.CREATED,
    )

    # Relations
    user_uuid: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("users.uuid"), nullable=True
    )
    user: Mapped["User"] = relationship("User", back_populates="bar_orders")

    drink_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("drinks.id"), nullable=True
    )
    drink: Mapped["Drink"] = relationship("Drink", back_populates="bar_orders")

    storage_order_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ingredients_storage.id"), nullable=True
    )
    storage_order: Mapped["IngredientStorage"] = relationship(
        "IngredientStorage", back_populates="bar_orders"
    )
