from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.connection import (
    SessionLocal
)

from app.models.pasajero import (
    Pasajero
)

from app.state.modo_claro import (
    ModoClaro
)

from app.state.modo_oscuro import (
    ModoOscuro
)

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/tema")

def obtener_tema(
    db: Session = Depends(get_db)
):

    pasajero = db.query(
        Pasajero
    ).first()

    return {
        "tema":
        pasajero.tema
    }


@router.put("/tema/{modo}")

def cambiar_tema(
    modo: str,
    db: Session = Depends(get_db)
):

    pasajero = db.query(
        Pasajero
    ).first()

    if modo == "oscuro":

        estado = ModoOscuro()

    else:

        estado = ModoClaro()

    pasajero.tema = (
        estado.nombre()
    )

    db.commit()

    return {
        "tema":
        pasajero.tema
    }