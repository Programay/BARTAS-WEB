from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Enum, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database import Base
from backend.src.storage import constants

if TYPE_CHECKING:
    # For IDE type checking only
    from backend.src.drinks.models import IngredientNeeded
    from backend.src.orders.models import BarOrder


class IngredientStorage(Base):
    __tablename__ = "ingredients_storage"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    ingredient_type: Mapped[constants.IngredientTypes] = mapped_column(
        Enum(constants.IngredientTypes), nullable=False
    )
    ingredient_unit: Mapped[constants.IngredientUnits] = mapped_column(
        Enum(constants.IngredientUnits), nullable=False
    )
    storage_amount: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    with_alcohol: Mapped[bool] = mapped_column(Boolean, default=True)
    can_be_ordered: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relations
    bar_orders: Mapped[list["BarOrder"]] = relationship(
        "BarOrder", back_populates="storage_order"
    )
    ingredients_needed: Mapped[list["IngredientNeeded"]] = relationship(
        "IngredientNeeded", back_populates="ingredients_storage"
    )
    image_path: Mapped[str] = mapped_column(String, nullable=True)
