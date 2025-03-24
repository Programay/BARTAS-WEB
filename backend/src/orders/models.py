from uuid import uuid4

from sqlalchemy import Enum, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base
from ..orders import constants


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
    user_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("users.uuid"), nullable=True)
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
