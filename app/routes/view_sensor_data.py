from __future__ import annotations
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.apis.big_query.sensor_data import (
    create_sensor_data,
    get_initial_n_sensor_data,
    get_last_n_sensor_data,
    update_sensor_data_by_id,
    remove_sensor_data_by_id,
)
from app.core.models import SensorData

router = APIRouter()


@router.post("/big_query/sensor_data/create", tags=["Big Query - Sensor Data"])
async def view_create_sensor_data(sensorData: SensorData) -> dict[str, str]:
    item_encoded = jsonable_encoder(sensorData)
    response_query = create_sensor_data(item_encoded)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}


@router.get("/big_query/sensor_data/initial/{num}", tags=["Big Query - Sensor Data"])
async def view_sensor_initial_data(
    num: int,
) -> dict[str, list]:
    return {"response": get_initial_n_sensor_data(num)}


@router.get("/big_query/sensor_data/last/{num}", tags=["Big Query - Sensor Data"])
async def view_sensor_last_data(
    num: int,
) -> dict[str, list]:
    return {"response": get_last_n_sensor_data(num)}


@router.put("/big_query/sensor_data/update/{id}", tags=["Big Query - Sensor Data"])
async def view_sensor_initial_data(id: str, sensorData: SensorData) -> dict[str, str]:
    item_encoded = jsonable_encoder(sensorData)
    response_query = update_sensor_data_by_id(id, item_encoded)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}


@router.delete("/big_query/sensor_data/remove/{id}", tags=["Big Query - Sensor Data"])
async def view_remove_sensor_data_by_id(
    id: str,
) -> dict[str, str]:
    response_query = remove_sensor_data_by_id(id)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}
