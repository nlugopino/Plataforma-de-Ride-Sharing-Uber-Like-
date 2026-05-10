from pydantic import BaseModel
from app.schemas.vehiculo_schema import VehiculoCreate, VehiculoResponse

class ConductorCreate(BaseModel):
    documento: str
    nombre: str
    correo: str
    telefono: str
    vehiculo: VehiculoCreate

class ConductorResponse(BaseModel):
    id: int
    documento: str
    nombre: str
    correo: str
    telefono: str
    vehiculo: VehiculoResponse

    class Config:
        orm_mode = True