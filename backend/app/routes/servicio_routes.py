from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import random

from app.database.connection import SessionLocal

from app.models.servicio import Servicio
from app.models.pasajero import Pasajero
from app.models.conductor import Conductor

from app.schemas.servicio_schema import (
    ServicioCreate,
    ServicioResponse
)

from app.services.facade.facade_servicio import FacadeServicio

router = APIRouter()

facade = FacadeServicio()


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# CREAR SERVICIO
@router.post("/servicios")
def crear_servicio(
    data: ServicioCreate,
    db: Session = Depends(get_db)
):

    pasajero = db.query(Pasajero).first()

    if not pasajero:
        raise HTTPException(
            status_code=404,
            detail="No existe pasajero"
        )

    servicio = facade.solicitar(
        db,
        data,
        pasajero.id
    )

    return servicio


# OBTENER SERVICIO ACTIVO PASAJERO
@router.get("/servicios/pasajero")
def obtener_servicio_pasajero(
    db: Session = Depends(get_db)
):

    pasajero = db.query(Pasajero).first()

    servicio = db.query(Servicio).filter(
        Servicio.pasajero_id == pasajero.id,
        Servicio.estado.in_(["pendiente", "aceptado"])
    ).first()

    return servicio


# CANCELAR
@router.put("/servicios/cancelar/{uuid_servicio}")
def cancelar(
    uuid_servicio: str,
    db: Session = Depends(get_db)
):

    servicio = db.query(Servicio).filter(
        Servicio.uuid_servicio == uuid_servicio
    ).first()

    if not servicio:
        raise HTTPException(
            status_code=404,
            detail="Servicio no encontrado"
        )

    return facade.cancelar(db, servicio)


# LISTADO CONDUCTOR
@router.get("/servicios/disponibles")
def disponibles(
    db: Session = Depends(get_db)
):

    return db.query(Servicio).filter(
        Servicio.estado == "pendiente"
    ).all()


# SERVICIO ACTIVO CONDUCTOR
@router.get("/servicios/conductor")
def servicio_conductor(
    db: Session = Depends(get_db)
):

    conductor = db.query(Conductor).first()

    servicio = db.query(Servicio).filter(
        Servicio.conductor_id == conductor.id,
        Servicio.estado == "aceptado"
    ).first()

    return servicio


# ACEPTAR
@router.put("/servicios/aceptar/{id_servicio}")
def aceptar(
    id_servicio: int,
    db: Session = Depends(get_db)
):

    conductor = db.query(Conductor).first()

    servicio = db.query(Servicio).filter(
        Servicio.id == id_servicio
    ).first()

    return facade.aceptar(
        db,
        servicio,
        conductor.id
    )


# FINALIZAR
@router.put("/servicios/finalizar/{id_servicio}")
def finalizar(
    id_servicio: int,
    db: Session = Depends(get_db)
):

    servicio = db.query(Servicio).filter(
        Servicio.id == id_servicio
    ).first()

    return facade.finalizar(
        db,
        servicio
    )