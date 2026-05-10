from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ServicioCreate(BaseModel):

    direccion_origen: str
    direccion_destino: str

    tipo_servicio: str

    distancia_km: float

    valor_oferta: float


class ServicioResponse(BaseModel):

    id: int

    uuid_servicio: str

    direccion_origen: str
    direccion_destino: str

    tipo_servicio: str

    distancia_km: float

    valor_oferta: float

    estado: str

    fecha_solicitud: datetime

    conductor_id: Optional[int]

    calificacion: Optional[int] = None

    comentario_calificacion: Optional[str] = None

    class Config:
        from_attributes = True

class CalificacionRequest(BaseModel):
    calificacion: int
    comentario: Optional[str] = None