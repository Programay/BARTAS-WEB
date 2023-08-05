import enum


class IngredientTypes(enum.Enum):
    """Possible ingredient types."""

    LIQUID = "LIQUID"
    BEER = "BEER"
    FRUIT = "FRUIT"
    VEGETABLE = "VEGETABLE"
    SNACK = "SNACK"
    OTHER = "OTHER"


class IngredientUnits(enum.Enum):
    """Possible ingredient units."""

    MILLILITER = "MILLILITER"
    PIECE = "PIECE"
    PACK = "PACK"
