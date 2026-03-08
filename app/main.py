from fastapi import FastAPI
from pydantic import BaseModel

from factories.fabrica_normal import FabricaViajeNormal
from factories.fabrica_premium import FabricaViajePremium
from models.viaje import Viaje

app = FastAPI()


# Modelo que define el body del request
class SolicitudViaje(BaseModel):
    tipo: str
    distancia_km: float


@app.post("/viaje")
def crear_viaje(datos: SolicitudViaje):

    if datos.tipo == "normal":
        fabrica = FabricaViajeNormal()

    elif datos.tipo == "premium":
        fabrica = FabricaViajePremium()

    else:
        return {"error": "Tipo de viaje no válido"}

    servicio_tarifa = fabrica.crear_servicio_tarifa()

    tarifa = servicio_tarifa.calcular_tarifa(datos.distancia_km)

    viaje = Viaje(datos.distancia_km, tarifa)

    return {
        "tipo": datos.tipo,
        "distancia": datos.distancia_km,
        "tarifa": tarifa
    }