from fastapi import APIRouter

from app.services.facade.facade_servicio import FacadeServicio

router = APIRouter()

facade = FacadeServicio()


@router.get("/notificaciones")

def obtener_notificacion():

    return {
        "mensaje":
        facade.observer.ultima_notificacion
    }