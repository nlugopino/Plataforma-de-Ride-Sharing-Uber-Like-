from pydantic import BaseModel

class PasajeroCreate(BaseModel):
    documento: str
    nombre: str
    correo: str
    telefono: str

class PasajeroResponse(PasajeroCreate):
    id: int

    class Config:
        orm_mode = True