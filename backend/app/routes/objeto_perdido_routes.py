from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.connection import (
    SessionLocal
)

from app.models.servicio import (
    Servicio
)

from app.models.objeto_perdido import (
    ObjetoPerdido
)

from app.schemas.objeto_perdido_schema import (
    ObjetoPerdidoRequest
)

from app.factory.objeto_perdido_factory import (
    ObjetoPerdidoFactory
)

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post(
    "/objetos-perdidos/{servicio_id}"
)
def reportar_objeto(
    servicio_id: int,
    data: ObjetoPerdidoRequest,
    db: Session = Depends(get_db)
):

    servicio = db.query(
        Servicio
    ).filter(
        Servicio.id == servicio_id
    ).first()

    if not servicio:

        raise HTTPException(
            status_code=404,
            detail="Servicio no encontrado"
        )

    if servicio.tiene_objeto_perdido:

        raise HTTPException(
            status_code=400,
            detail="Ya existe un reporte"
        )

    objeto = (
        ObjetoPerdidoFactory.crear(
            data.tipo,
            data.descripcion
        )
    )

    reporte = ObjetoPerdido(

        tipo=data.tipo,

        descripcion=
        objeto.descripcion,

        servicio_id=
        servicio.id
    )

    db.add(reporte)

    servicio.tiene_objeto_perdido = True

    db.commit()

    return {
        "mensaje":
        "Reporte creado"
    }