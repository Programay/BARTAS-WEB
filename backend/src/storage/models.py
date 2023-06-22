from sqlalchemy import Column, Integer, String, Enum, Boolean
from sqlalchemy.orm import relationship

from . import constants
from ..database import Base


class IngredientStorage(Base):
    __tablename__ = "ingredient_storage"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, index=True, nullable=False)

    ingredient_type = Column(Enum(constants.IngredientTypes), nullable=False)
    ingredient_unit = Column(Enum(constants.IngredientUnits), nullable=False)

    storage_amount = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    with_alcohol = Column(Boolean, default=True)
    can_be_ordered = Column(Boolean, default=False)

    ingredients_needed = relationship("IngredientNeeded", back_populates="ingredients_storage")

    # image = Column() # TODO Add image storing
