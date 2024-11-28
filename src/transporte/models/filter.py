from pydantic import BaseModel
from typing import Optional


class FilterSchema(BaseModel):
    centro: Optional[str] = None
    usuario_conteo: Optional[str] = None
    estado: Optional[str] = None

    