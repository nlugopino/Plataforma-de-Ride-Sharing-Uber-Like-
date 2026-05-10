from pydantic import BaseModel

class VehiculoCreate(BaseModel):
    tipo_vehiculo: str
    placa: str
    modelo: int
    cilindraje: int

class VehiculoResponse(VehiculoCreate):
    id: int

    class Config:
        orm_mode = True