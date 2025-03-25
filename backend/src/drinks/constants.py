from enum import StrEnum


class ComplicatedLevels(StrEnum):
    """Complicated drink level."""

    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class DrinkTypes(StrEnum):
    """Possible drink types."""

    ONE_SHOT = "ONE SHOT"
    MULTIPLE_SHOT = "MULTIPLE SHOT"
    DRINK = "DRINK"
