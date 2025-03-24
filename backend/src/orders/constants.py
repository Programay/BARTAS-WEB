from enum import StrEnum


class OrderStatus(StrEnum):
    """Available status for order."""

    CREATED = "created"
    ACCEPTED = "accepted"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    REJECTED = "rejected"
    CANCELED = "canceled"
