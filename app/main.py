from typing import Any

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from .schemas import (
    ShipmentCreate,
    ShipmentRead,
    ShipmentUpdate,
)

app = FastAPI()

shipments = {
    1234: {
        "weight": 0.9,
        "content": "Glass door",
        "status": "placed",
        "destination": 10001,
    },
    1235: {
        "weight": 1.2,
        "content": "Wooden chair",
        "status": "in transit",
        "destination": 10002,
    },
    1236: {
        "weight": 2.5,
        "content": "Metal desk",
        "status": "delivered",
        "destination": 10003,
    },
    1237: {
        "weight": 0.5,
        "content": "Plastic box",
        "status": "placed",
        "destination": 10004,
    },
    1238: {
        "weight": 3.0,
        "content": "Bookshelf",
        "status": "in transit",
        "destination": 10005,
    },
    1239: {
        "weight": 1.5,
        "content": "Lamp",
        "status": "delivered",
        "destination": 10006,
    },
    1240: {
        "weight": 2.0,
        "content": "Cabinet",
        "status": "placed",
        "destination": 10007,
    },
}


@app.get("/shipment/latest")
def get_latest_shipment():
    id = max(shipments.keys())
    return shipments[id]


@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id: int):

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given id does not exist!!"
        )

    return shipments[id]


@app.post("/shipment")
def submit_shipment(shipment: ShipmentCreate) -> dict[str, Any]:
    if shipment.weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Maximum Weight limit is 25 kgs",
        )

    new_id = max(shipments.keys()) + 1

    shipments[new_id] = {
        "content": shipment.content,
        "weight": shipment.weight,
        "destination": shipment.destination,
        "status": "placed",
    }

    return {"id": new_id}


@app.get("/shipment/{field}")
def get_shipment_field(field: str, id: int) -> dict[str, Any]:
    return {field: shipments[id][field]}


@app.put("/shipment")
def shipment_update(
    id: int,
    content: str,
    weight: float,
    status: str,
) -> dict[str, Any]:
    shipments[id] = {
        "content": content,
        "weight": weight,
        "status": status,
    }

    return shipments[id]


@app.patch("/shipment", response_model=ShipmentRead)
def update_shipment(
    id: int,
    body: ShipmentUpdate,
):
    shipment = shipments[id]
    shipment.update(body)
    return shipment


@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, Any]:
    shipments.pop(id)
    return {"detail": f"Shipment with id #{id} is deleted!"}


@app.get("/scalar")
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
