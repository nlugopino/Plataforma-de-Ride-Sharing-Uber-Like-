from fastapi import (
    APIRouter,
    Depends
)

from fastapi.responses import (
    FileResponse
)

from sqlalchemy.orm import Session

from datetime import datetime

from app.database.connection import (
    SessionLocal
)

from app.models.conductor import (
    Conductor
)

from app.models.servicio import (
    Servicio
)

from app.builders.reporte_mensual_builder import (
    ReporteMensualBuilder
)

from app.builders.director_reporte import (
    DirectorReporte
)

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get(
    "/reportes/mensual/{mes}/{anio}"
)
def generar_reporte(
    mes: int,
    anio: int,
    db: Session = Depends(get_db)
):

    conductor = db.query(
        Conductor
    ).first()

    servicios = db.query(
        Servicio
    ).filter(
        Servicio.conductor_id
        ==
        conductor.id
    ).all()

    servicios = [

        s for s in servicios

        if
        s.fecha_finalizacion
        and
        s.fecha_finalizacion.month
        == mes
        and
        s.fecha_finalizacion.year
        == anio

    ]

    builder = (
        ReporteMensualBuilder(
            conductor,
            servicios,
            mes,
            anio
        )
    )

    director = DirectorReporte(
        builder
    )

    ruta = director.construir()

    return FileResponse(
        ruta,
        media_type="application/pdf",
        filename=
        f"reporte_{mes}_{anio}.pdf"
    )