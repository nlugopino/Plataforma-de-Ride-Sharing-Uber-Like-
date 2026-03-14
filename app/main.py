from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from core.configuracion import ConfiguracionApp
from factories.fabrica_normal import FabricaViajeNormal
from factories.fabrica_premium import FabricaViajePremium
from models.viaje import Viaje

app = FastAPI()

# Modelo que define el body del request
class SolicitudViaje(BaseModel):
    tipo: str
    distancia_km: float
    propina: Optional[float] = None
    descuento: Optional[float] = None

@app.get("/test-singleton")
def probar_singleton():

    config1 = ConfiguracionApp()
    config2 = ConfiguracionApp()

    print("ID instancia 1:", id(config1))
    print("ID instancia 2:", id(config2))

    return {
        "tarifa_base": config1.tarifa_base,
        "precio_por_km": config1.precio_por_km,
        "misma_instancia": id(config1) == id(config2)
    }

@app.post("/viaje")
def crear_viaje(datos: SolicitudViaje):

    if datos.tipo == "normal":
        print("🟡 [Factory Method] Seleccionando FabricaViajeNormal")
        fabrica = FabricaViajeNormal()

    elif datos.tipo == "premium":
        print("🟡 [Factory Method] Seleccionando FabricaViajePremium")
        fabrica = FabricaViajePremium()

    servicio_tarifa = fabrica.crear_servicio_tarifa(
        datos.propina,
        datos.descuento
    )

    tarifa = servicio_tarifa.calcular_tarifa(datos.distancia_km)

    return {
        "tipo": datos.tipo,
        "distancia": datos.distancia_km,
        "tarifa": tarifa
    }