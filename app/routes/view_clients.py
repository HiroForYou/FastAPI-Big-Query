from __future__ import annotations

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.apis.api_1.clients import (
    create_client,
    get_initial_n_clients,
    get_last_n_clients,
    remove_client_by_id,
    update_client_by_id,
)
from app.core.models import Client

router = APIRouter()


@router.post("/api_1/client/create", tags=["API 1 - Clients"])
async def view_create_client(sensorData: Client) -> dict[str, list]:
    item_encoded = jsonable_encoder(sensorData)
    response_query = create_client(item_encoded)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}


@router.get("/api_1/client/initial/{num}", tags=["API 1 - Clients"])
async def view_clients_initial(
    num: int,
) -> dict[str, list]:
    return {"response": get_initial_n_clients(num)}


@router.get("/api_1/client/last/{num}", tags=["API 1 - Clients"])
async def view_clients_last(
    num: int,
) -> dict[str, list]:
    return {"response": get_last_n_clients(num)}


@router.put("/api_1/client/update/{id}", tags=["API 1 - Clients"])
async def view_update_client_by_id(id: str, sensorData: Client) -> dict[str, list]:
    item_encoded = jsonable_encoder(sensorData)
    response_query = update_client_by_id(id, item_encoded)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}


@router.delete("/api_1/client/remove/{id}", tags=["API 1 - Clients"])
async def view_remove_client_by_id(
    id: str,
) -> dict[str, list]:
    response_query = remove_client_by_id(id)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}
