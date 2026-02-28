from fastapi import FastAPI
from factories.fabrica_viaje import FabricaViaje

app = FastAPI()

@app.post("/viaje")
def crear_viaje(distancia_km: float):
    # Se delega la creación del viaje a la fábrica
    viaje = FabricaViaje.crear_viaje(distancia_km)
    return {
        "distancia_km": viaje.distancia_km,
        "tarifa": viaje.tarifa
    }