from sqlalchemy import Boolean, Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base
from . import constants


class IngredientStorage(Base):
    __tablename__ = "ingredients_storage"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, index=True, nullable=False)

    ingredient_type = Column(Enum(constants.IngredientTypes), nullable=False)
    ingredient_unit = Column(Enum(constants.IngredientUnits), nullable=False)

    storage_amount = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    with_alcohol = Column(Boolean, default=True)
    can_be_ordered = Column(Boolean, default=False)

    # Relations
    bar_orders = relationship("BarOrder", back_populates="storage_order")
    ingredients_needed = relationship(
        "IngredientNeeded", back_populates="ingredients_storage"
    )

    image_path = Column(String, nullable=True)
