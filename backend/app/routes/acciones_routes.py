from fastapi import APIRouter
from app.command.panel_acciones import PanelAcciones
from app.command.servicio_emergencia import ServicioEmergencia
from app.command.servicio_ubicacion import ServicioUbicacion
from app.command.servicio_contacto import ServicioContacto
from app.command.emergencia_command import EmergenciaCommand
from app.command.ubicacion_command import UbicacionCommand
from app.command.contacto_command import ContactoCommand

router = APIRouter()

panel = PanelAcciones()


@router.post("/acciones/emergencia")

def emergencia():

    command = EmergenciaCommand(
        ServicioEmergencia()
    )

    return {
        "mensaje":
        panel.ejecutar(command)
    }


@router.post("/acciones/ubicacion")

def ubicacion():

    command = UbicacionCommand(
        ServicioUbicacion()
    )

    return {
        "mensaje":
        panel.ejecutar(command)
    }


@router.post("/acciones/contacto")

def contacto():

    command = ContactoCommand(
        ServicioContacto()
    )

    return {
        "mensaje":
        panel.ejecutar(command)
    }