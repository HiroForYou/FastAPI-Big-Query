from __future__ import annotations

from fastapi import APIRouter, Depends

from app.apis.big_query.sensor_data import get_initial_n_data, get_last_n_data

router = APIRouter()


@router.get("/")
async def index() -> dict[str, str]:
    return {
        "info": "This is the index page of fastapi-big-query. "
        "You probably want to go to 'http://<hostname:port>/docs'.",
    }


@router.get("/big_query/sensor_data/initial/{num}", tags=["big_query"])
async def view_sensor_initial_data(
    num: int,
) -> dict[str, list]:
    return {"response": get_initial_n_data(num)}


@router.get("/big_query/sensor_data/last/{num}", tags=["big_query"])
async def view_sensor_last_data(
    num: int,
) -> dict[str, list]:
    return {"response": get_last_n_data(num)}
