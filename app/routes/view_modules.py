from __future__ import annotations

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.apis.api_1.modules import (
    create_module,
    get_initial_n_modules,
    get_last_n_modules,
    remove_module_by_id,
    update_module_by_id,
)
from app.core.models import Module

router = APIRouter()


@router.post("/api_1/module/create", tags=["API 1 - Modules"])
async def view_create_module(module: Module) -> dict[str, list]:
    item_encoded = jsonable_encoder(module)
    response_query = create_module(item_encoded)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}


@router.get("/api_1/module/initial/{num}", tags=["API 1 - Modules"])
async def view_modules_initial(
    num: int,
) -> dict[str, list]:
    return {"response": get_initial_n_modules(num)}


@router.get("/api_1/module/last/{num}", tags=["API 1 - Modules"])
async def view_modules_last(
    num: int,
) -> dict[str, list]:
    return {"response": get_last_n_modules(num)}


@router.put("/api_1/module/update/{id}", tags=["API 1 - Modules"])
async def view_update_module_by_id(id: str, module: Module) -> dict[str, list]:
    item_encoded = jsonable_encoder(module)
    response_query = update_module_by_id(id, item_encoded)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}


@router.delete("/api_1/module/remove/{id}", tags=["API 1 - Modules"])
async def view_remove_module_by_id(
    id: str,
) -> dict[str, list]:
    response_query = remove_module_by_id(id)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}
