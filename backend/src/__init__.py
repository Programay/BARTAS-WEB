from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    date_creation: Mapped[datetime] = mapped_column(server_default=func.now())
    date_modified: Mapped[datetime] = mapped_column(onupdate=func.now(), nullable=True)


from .drinks.models import Drink, IngredientNeeded
from .orders.models import BarOrder
from .storage.models import IngredientStorage
from .users.models import User
