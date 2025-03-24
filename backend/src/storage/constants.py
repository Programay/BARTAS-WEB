from enum import StrEnum


class IngredientTypes(StrEnum):
    """Possible ingredient types."""

    LIQUID = "LIQUID"
    BEER = "BEER"
    FRUIT = "FRUIT"
    VEGETABLE = "VEGETABLE"
    SNACK = "SNACK"
    OTHER = "OTHER"


class IngredientUnits(StrEnum):
    """Possible ingredient units."""

    MILLILITER = "MILLILITER"
    PIECE = "PIECE"
    PACK = "PACK"
