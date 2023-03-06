from __future__ import annotations
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.apis.big_query.clients import (
    create_client,
    get_initial_n_clients,
    get_last_n_clients,
    update_client_by_id,
    remove_client_by_id,
)
from app.core.models import Client

router = APIRouter()


@router.post("/big_query/client/create", tags=["Big Query - Clients"])
async def view_create_client(sensorData: Client) -> dict[str, list]:
    item_encoded = jsonable_encoder(sensorData)
    response_query = create_client(item_encoded)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}


@router.get("/big_query/client/initial/{num}", tags=["Big Query - Clients"])
async def view_clients_initial(
    num: int,
) -> dict[str, list]:
    return {"response": get_initial_n_clients(num)}


@router.get("/big_query/client/last/{num}", tags=["Big Query - Clients"])
async def view_clients_last(
    num: int,
) -> dict[str, list]:
    return {"response": get_last_n_clients(num)}


@router.put("/big_query/client/update/{id}", tags=["Big Query - Clients"])
async def view_update_client_by_id(id: str, sensorData: Client) -> dict[str, list]:
    item_encoded = jsonable_encoder(sensorData)
    response_query = update_client_by_id(id, item_encoded)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}


@router.delete("/big_query/client/remove/{id}", tags=["Big Query - Clients"])
async def view_remove_client_by_id(
    id: str,
) -> dict[str, list]:
    response_query = remove_client_by_id(id)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}
