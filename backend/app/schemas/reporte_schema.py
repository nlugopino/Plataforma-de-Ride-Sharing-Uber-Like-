from pydantic import BaseModel
from typing import Optional

class ReporteRequest(BaseModel):

    tipo_incidente: str

    descripcion: Optional[str] = None


class ReporteResponse(BaseModel):

    id: int

    servicio_id: int

    tipo_incidente: str

    descripcion: Optional[str]

    estado: str

    class Config:
        from_attributes = True