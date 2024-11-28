from pydantic import BaseModel
from typing import Optional

class UpdateTransporte(BaseModel):
    id : str
    Cantdiad_fisica: Optional[str] = None
    fecha_hora_conteo: Optional[str] = None
    estado: Optional[str] = None