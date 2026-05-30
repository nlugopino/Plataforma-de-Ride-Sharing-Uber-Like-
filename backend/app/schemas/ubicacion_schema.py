from pydantic import BaseModel


class UbicacionCreate(BaseModel):

    tipo: str

    direccion: str


class UbicacionResponse(BaseModel):

    id: int

    tipo: str

    direccion: str

    class Config:

        orm_mode = True