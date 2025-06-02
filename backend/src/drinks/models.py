from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database import Base
from backend.src.drinks import constants

if TYPE_CHECKING:
    # For IDE type checking only
    from backend.src.orders.models import BarOrder
    from backend.src.storage.models import IngredientStorage


class Drink(Base):
    __tablename__ = "drinks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    complicated: Mapped[constants.ComplicatedLevels] = mapped_column(
        Enum(constants.ComplicatedLevels), nullable=False
    )
    drink_type: Mapped[constants.DrinkTypes] = mapped_column(
        Enum(constants.DrinkTypes), nullable=False
    )
    preparation_description: Mapped[str] = mapped_column(String, nullable=True)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    with_alcohol: Mapped[bool] = mapped_column(Boolean, default=True)
    is_possible_to_make: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relations
    bar_orders: Mapped[list["BarOrder"]] = relationship(
        "BarOrder", back_populates="drink"
    )
    ingredients_needed: Mapped[list["IngredientNeeded"]] = relationship(
        "IngredientNeeded",
        back_populates="drink",
        cascade="all,delete",
        passive_deletes=True,
    )
    image_path: Mapped[str] = mapped_column(String, nullable=True)


class IngredientNeeded(Base):
    __tablename__ = "ingredients_needed"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    amount_needed: Mapped[int] = mapped_column(Integer, nullable=False)
    is_enough_to_make_a_drink: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relations
    drink_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("drinks.id"), nullable=False
    )
    drink: Mapped["Drink"] = relationship("Drink", back_populates="ingredients_needed")
    ingredients_storage_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ingredients_storage.id")
    )
    ingredients_storage: Mapped["IngredientStorage"] = relationship(
        "IngredientStorage", back_populates="ingredients_needed"
    )
