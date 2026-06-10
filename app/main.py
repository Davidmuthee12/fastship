from typing import Any

from fastapi import FastAPI, HTTPException, status, Depends
from app.database.models import Shipment
from scalar_fastapi import get_scalar_api_reference
from .schemas import (
    ShipmentCreate,
    ShipmentRead,
    ShipmentUpdate,
)
from .database import Database
from app.database.session import create_db_tables, get_session
from contextlib import asynccontextmanager
from sqlmodel import Session


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    create_db_tables()
    yield


app = FastAPI(lifespan=lifespan_handler)
db = Database()


@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id: int, session: Session = Depends(get_session)):
    session
    # check for shipment with given id
    shipment = session.get(Shipment, id)

    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given id does not exist!!"
        )

    return shipment


@app.post("/shipment")
def submit_shipment(
    shipment: ShipmentCreate, session: Session = Depends(get_session)
) -> dict[str, Any]:
    new_id = db.create(shipment)

    return {"id": new_id}


@app.patch("/shipment", response_model=ShipmentRead)
def update_shipment(
    id: int,
    shipment: ShipmentUpdate,
):
    shipment = db.update(id, shipment)
    return shipment


@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, Any]:
    db.delete(id)
    return {"detail": f"Shipment with id #{id} is deleted!"}


@app.get("/scalar")
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
