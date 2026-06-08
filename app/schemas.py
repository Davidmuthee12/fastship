from random import randint

from pydantic import BaseModel, Field


def random_destination():
    randint(11000, 11999)


class shipment(BaseModel):
    content: str = Field(max_length=30)
    weight: float = Field(description="Weight must be in kgs", le=25, ge=1)
    destination: int | None = Field(
        default_factory=random_destination,
    )
