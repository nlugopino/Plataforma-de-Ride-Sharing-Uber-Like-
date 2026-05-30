from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal

from app.models.pasajero import Pasajero
from app.models.ubicacion_frecuente import UbicacionFrecuente

from app.schemas.ubicacion_schema import (UbicacionCreate)

router = APIRouter()

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/ubicaciones")

def listar_ubicaciones(
    db: Session = Depends(get_db)
):

    pasajero = db.query(
        Pasajero
    ).first()

    return db.query(
        UbicacionFrecuente
    ).filter(
        UbicacionFrecuente.pasajero_id
        ==
        pasajero.id
    ).all()


@router.post("/ubicaciones")

def guardar_ubicaciones(
    data: list[UbicacionCreate],
    db: Session = Depends(get_db)
):

    pasajero = db.query(
        Pasajero
    ).first()

    db.query(
        UbicacionFrecuente
    ).filter(
        UbicacionFrecuente.pasajero_id
        ==
        pasajero.id
    ).delete()

    for item in data:

        nueva = UbicacionFrecuente(

            tipo=item.tipo,

            direccion=item.direccion,

            pasajero_id=pasajero.id
        )

        db.add(nueva)

    db.commit()

    return {
        "mensaje":
        "Ubicaciones guardadas"
    }