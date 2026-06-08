from random import randint
from enum import Enum

from pydantic import BaseModel, Field


def random_destination():
    randint(11000, 11999)


class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"


class Shipment(BaseModel):
    content: str
    weight: float = Field(le=25)
    destination: int
    status: ShipmentStatus
