from fastapi import APIRouter
from .service import getTrasportes, updateTransporte
from .models.filter import FilterSchema
from .models.updateTransporte import UpdateTransporte
from typing import Optional, List

router = APIRouter(
    prefix="/transporte",
    tags=["Transporte"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def root(filter: Optional[FilterSchema] = None):
    return await getTrasportes(filter)

@router.put("/")
async def root(schema: List[UpdateTransporte]):
    return await updateTransporte(schema)