from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from . import utils
from ..database import Base


class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, index=True, nullable=False)

    complicated = Column(Enum(utils.ComplicatedLevels), nullable=False)
    drink_type = Column(Enum(utils.DrinkTypes), nullable=False)
    preparation_description = Column(String, nullable=True)

    amount = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

    with_alcohol = Column(Boolean, default=True)
    is_possible_to_make = Column(Boolean, default=False)

    ingredients_needed = relationship("IngredientNeeded", back_populates="drink", cascade="all,delete",
                                      passive_deletes=True)

    # image = Column() # TODO Add image storing


class IngredientNeeded(Base):
    __tablename__ = "ingredient_needed"

    id = Column(Integer, primary_key=True, index=True)

    drink_id = Column(Integer, ForeignKey("drinks.id"), nullable=False)
    drink = relationship("Drink", back_populates="ingredients_needed")
    ingredients_storage = relationship("IngredientStorage", back_populates="ingredients_needed")

    amount_needed = Column(Integer, nullable=False)

    is_enough_to_make_a_drink = Column(Boolean, default=False)
