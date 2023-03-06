from __future__ import annotations
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.apis.big_query.modules import (
    create_module,
    get_initial_n_modules,
    get_last_n_modules,
    update_module_by_id,
    remove_module_by_id,
)
from app.core.models import Module

router = APIRouter()


@router.post("/big_query/module/create", tags=["Big Query - Modules"])
async def view_create_module(module: Module) -> dict[str, list]:
    item_encoded = jsonable_encoder(module)
    response_query = create_module(item_encoded)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}


@router.get("/big_query/module/initial/{num}", tags=["Big Query - Modules"])
async def view_modules_initial(
    num: int,
) -> dict[str, list]:
    return {"response": get_initial_n_modules(num)}


@router.get("/big_query/module/last/{num}", tags=["Big Query - Modules"])
async def view_modules_last(
    num: int,
) -> dict[str, list]:
    return {"response": get_last_n_modules(num)}


@router.put("/big_query/module/update/{id}", tags=["Big Query - Modules"])
async def view_update_module_by_id(id: str, module: Module) -> dict[str, list]:
    item_encoded = jsonable_encoder(module)
    response_query = update_module_by_id(id, item_encoded)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}


@router.delete("/big_query/module/remove/{id}", tags=["Big Query - Modules"])
async def view_remove_module_by_id(
    id: str,
) -> dict[str, list]:
    response_query = remove_module_by_id(id)
    if not response_query:
        raise HTTPException(status_code=500, detail="Server internal error!")
    return {"response": response_query}
