from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.database.connection import SessionLocal

from app.models.conductor import Conductor
from app.models.vehiculo import Vehiculo

from app.schemas.conductor_schema import (
    ConductorCreate,
    ConductorResponse
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/conductores")
def guardar_conductor(
    conductor: ConductorCreate,
    db: Session = Depends(get_db)
):

    existente = db.query(Conductor).first()

    if existente:

        existente.documento = conductor.documento
        existente.nombre = conductor.nombre
        existente.correo = conductor.correo
        existente.telefono = conductor.telefono

        if existente.vehiculo:
            existente.vehiculo.tipo_vehiculo = conductor.vehiculo.tipo_vehiculo
            existente.vehiculo.placa = conductor.vehiculo.placa
            existente.vehiculo.modelo = conductor.vehiculo.modelo
            existente.vehiculo.cilindraje = conductor.vehiculo.cilindraje

        db.commit()
        db.refresh(existente)

        return existente

    nuevo_conductor = Conductor(
        documento=conductor.documento,
        nombre=conductor.nombre,
        correo=conductor.correo,
        telefono=conductor.telefono
    )

    db.add(nuevo_conductor)
    db.commit()
    db.refresh(nuevo_conductor)

    nuevo_vehiculo = Vehiculo(
        tipo_vehiculo=conductor.vehiculo.tipo_vehiculo,
        placa=conductor.vehiculo.placa,
        modelo=conductor.vehiculo.modelo,
        cilindraje=conductor.vehiculo.cilindraje,
        conductor_id=nuevo_conductor.id
    )

    db.add(nuevo_vehiculo)
    db.commit()

    return nuevo_conductor

@router.get("/conductores", response_model=ConductorResponse)
def obtener_conductor(
    db: Session = Depends(get_db)
):

    conductor = db.query(Conductor).first()

    if not conductor:
        raise HTTPException(
            status_code=404,
            detail="No existe conductor"
        )

    return conductor