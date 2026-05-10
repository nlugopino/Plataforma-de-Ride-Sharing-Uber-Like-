from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.database.connection import SessionLocal
from app.models.pasajero import Pasajero
from app.schemas.pasajero_schema import (
    PasajeroCreate,
    PasajeroResponse
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear o actualizar
@router.post("/pasajeros")
def guardar_pasajero(
    pasajero: PasajeroCreate,
    db: Session = Depends(get_db)
):

    existente = db.query(Pasajero).first()

    if existente:
        existente.documento = pasajero.documento
        existente.nombre = pasajero.nombre
        existente.correo = pasajero.correo
        existente.telefono = pasajero.telefono

        db.commit()
        db.refresh(existente)

        return existente

    nuevo = Pasajero(**pasajero.dict())

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo

# Obtener único pasajero
@router.get("/pasajeros", response_model=PasajeroResponse)
def obtener_pasajero(
    db: Session = Depends(get_db)
):

    pasajero = db.query(Pasajero).first()

    if not pasajero:
        raise HTTPException(
            status_code=404,
            detail="No existe pasajero"
        )

    return pasajero