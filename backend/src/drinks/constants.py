import enum


class ComplicatedLevels(enum.Enum):
    """Complicated drink level."""

    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class DrinkTypes(enum.Enum):
    """Possible drink types."""

    ONE_SHOT = "ONE SHOT"
    MULTIPLE_SHOT = "MULTIPLE SHOT"
    DRINK = "DRINK"
