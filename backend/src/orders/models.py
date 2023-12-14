from uuid import uuid4

from sqlalchemy import Column, Enum, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ..database import Base
from . import constants


class BarOrder(Base):
    __tablename__ = "bar_orders"

    uuid = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)

    status = Column(
        Enum(constants.OrderStatus),
        nullable=False,
        default=constants.OrderStatus.CREATED,
    )

    # Relations
    user_id = Column(UUID, ForeignKey("users.uuid"), nullable=True)
    user = relationship("User", back_populates="bar_orders")

    drink_id = Column(Integer, ForeignKey("drinks.id"), nullable=True)
    drink = relationship("Drink", back_populates="bar_orders")

    storage_order_id = Column(
        Integer, ForeignKey("ingredients_storage.id"), nullable=True
    )
    storage_order = relationship("IngredientStorage", back_populates="bar_orders")
