from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.models.servicio import Servicio
from app.models.reporte_incidente import ReporteIncidente

from app.schemas.reporte_schema import (
    ReporteRequest,
    ReporteResponse
)

from app.builders.reporte_builder import ReporteBuilder

from typing import Optional

router = APIRouter()

# CREAR REPORTE
@router.post(
    "/servicios/{servicio_id}/reportar"
)
def reportar_incidente(
    servicio_id: int,
    data: ReporteRequest,
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

    reporte_existente = db.query(
        ReporteIncidente
    ).filter(
        ReporteIncidente.servicio_id == servicio_id
    ).first()

    if reporte_existente:
        raise HTTPException(
            status_code=400,
            detail="Este viaje ya tiene un reporte"
        )

    reporte = (
        ReporteBuilder()
        .set_servicio(servicio_id)
        .set_tipo(data.tipo_incidente)
        .set_descripcion(data.descripcion)
        .set_estado()
        .build()
    )

    db.add(reporte)

    db.commit()

    return {
        "mensaje": "Reporte enviado"
    }


# CONSULTAR REPORTE
@router.get(
    "/servicios/{servicio_id}/reporte",
    response_model=Optional[ReporteResponse]
)
def obtener_reporte(
    servicio_id: int,
    db: Session = Depends(get_db)
):

    reporte = db.query(
        ReporteIncidente
    ).filter(
        ReporteIncidente.servicio_id == servicio_id
    ).first()

    return reporte