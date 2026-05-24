from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import random

from app.database.connection import SessionLocal

from app.models.servicio import Servicio
from app.models.pasajero import Pasajero
from app.models.conductor import Conductor

from app.schemas.servicio_schema import (
    ServicioCreate,
    ServicioResponse,
    CalificacionRequest
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

    try : 

        return facade.cancelar(db, servicio)
    
    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

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

    try:

        return facade.aceptar(
            db,
            servicio,
            conductor.id
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
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

    try :

        return facade.finalizar(
            db,
            servicio
        )
    
    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.post("/servicios/{servicio_id}/calificar")
def calificar_servicio(
    servicio_id: int,
    data: CalificacionRequest,
    db: Session = Depends(get_db)
):

    servicio = db.query(Servicio).filter(
        Servicio.id == servicio_id
    ).first()

    if not servicio:
        raise HTTPException(
            status_code=404,
            detail="Servicio no encontrado"
        )

    if servicio.estado != "finalizado":
        raise HTTPException(
            status_code=400,
            detail="Solo se pueden calificar viajes finalizados"
        )

    if servicio.calificacion is not None:
        raise HTTPException(
            status_code=400,
            detail="Este viaje ya fue calificado"
        )

    if data.calificacion < 1 or data.calificacion > 5:
        raise HTTPException(
            status_code=400,
            detail="La calificación debe estar entre 1 y 5"
        )

    servicio.calificacion = data.calificacion
    servicio.comentario_calificacion = data.comentario

    db.commit()
    db.refresh(servicio)

    return {
        "mensaje": "Calificación registrada"
    }

@router.get("/servicios/historial/{pasajero_id}",
response_model=list[ServicioResponse])
def historial_viajes(
    pasajero_id: int,
    db: Session = Depends(get_db)
):

    servicios = db.query(Servicio).filter(
        Servicio.pasajero_id == pasajero_id,
        Servicio.estado == "finalizado"
    ).all()

    return servicios