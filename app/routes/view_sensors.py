from __future__ import annotations

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.apis.api_1.sensors import (
    create_sensor,
    get_initial_n_sensors,
    get_last_n_sensors,
    remove_sensor_by_id,
    update_sensor_by_id,
)
from app.core.models import Sensor

router = APIRouter()


@router.post("/api_1/sensor/create", tags=["API 1 - Sensors"])
async def view_create_sensor(sensor: Sensor) -> dict[str, list]:
    item_encoded = jsonable_encoder(sensor)
    response_query = create_sensor(item_encoded)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}


@router.get("/api_1/sensor/initial/{num}", tags=["API 1 - Sensors"])
async def view_sensors_initial(
    num: int,
) -> dict[str, list]:
    return {"response": get_initial_n_sensors(num)}


@router.get("/api_1/sensor/last/{num}", tags=["API 1 - Sensors"])
async def view_sensors_last(
    num: int,
) -> dict[str, list]:
    return {"response": get_last_n_sensors(num)}


@router.put("/api_1/sensor/update/{id}", tags=["API 1 - Sensors"])
async def view_update_sensor_by_id(id: str, sensor: Sensor) -> dict[str, list]:
    item_encoded = jsonable_encoder(sensor)
    response_query = update_sensor_by_id(id, item_encoded)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}


@router.delete("/api_1/sensor/remove/{id}", tags=["API 1 - Sensors"])
async def view_remove_sensor_by_id(
    id: str,
) -> dict[str, list]:
    response_query = remove_sensor_by_id(id)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}
