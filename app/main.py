from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from core.configuracion import ConfiguracionApp
from factories.fabrica_normal import FabricaViajeNormal
from factories.fabrica_premium import FabricaViajePremium
from models.viaje import Viaje
from prototypes.configuracion_viaje import ConfiguracionViaje
from adapters.adapter_mapa_a import AdapterMapaA
from adapters.adapter_mapa_b import AdapterMapaB
from bridge.email import Email
from bridge.sms import SMS
from bridge.notificacion_viaje import NotificacionViaje
from bridge.notificacion_emergencia import NotificacionEmergencia
from decorators.tarifa_base import TarifaBase
from decorators.peaje import Peaje
from decorators.nocturno import Nocturno
from decorators.seguro import Seguro
from facade.facade_viaje import FacadeFinalizarViaje
from composite.servicio_individual import ServicioIndividual
from composite.paquete_servicios import PaqueteServicios

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

@app.get("/test-factory")
def probar_factory(tipo: str):

    if tipo == "normal":
        print("🟡 [Factory Method] Creando fábrica NORMAL")
        fabrica = FabricaViajeNormal()

    elif tipo == "premium":
        print("🟡 [Factory Method] Creando fábrica PREMIUM")
        fabrica = FabricaViajePremium()

    else:
        return {"error": "Tipo no válido"}

    servicio = fabrica.crear_servicio_tarifa()

    return {
        "mensaje": f"Servicio creado para viaje {tipo}",
        "tipo_servicio": type(servicio).__name__
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

@app.post("/viaje-builder")
def crear_viaje_builder(datos: SolicitudViaje):

    if datos.tipo == "normal":
        fabrica = FabricaViajeNormal()
    else:
        fabrica = FabricaViajePremium()

    servicio_tarifa = fabrica.crear_servicio_tarifa(
        datos.propina,
        datos.descuento
    )

    tarifa = servicio_tarifa.calcular_tarifa(datos.distancia_km)

    from builders.viaje_builder_concreto import ViajeBuilder

    builder = ViajeBuilder()

    viaje = (
        builder
        .agregar_distancia(datos.distancia_km)
        .agregar_tarifa(tarifa)
        .agregar_propina(datos.propina)
        .construir()
    )

    return {
        "distancia": viaje.distancia,
        "tarifa": viaje.tarifa,
        "propina": viaje.propina,
        "total": viaje.total
    }

@app.get("/test-prototype")
def probar_prototype():

    # Configuración base
    config_base = ConfiguracionViaje(
        tipo="normal",
        seguridad=False,
        trafico="medio",
        prioridad="baja"
    )

    # Clonar configuración
    config_clon = config_base.clonar()

    # Modificar clon (importante 🔥)
    config_clon.tipo = "premium"
    config_clon.seguridad = True
    config_clon.prioridad = "alta"

    return {
        "original": config_base.mostrar(),
        "clon": config_clon.mostrar()
    }

@app.get("/test-adapter")
def probar_adapter(tipo: str):

    if tipo == "a":
        adapter = AdapterMapaA()

    elif tipo == "b":
        adapter = AdapterMapaB()

    else:
        return {"error": "Tipo no válido"}

    tiempo = adapter.obtener_tiempo("A", "B")

    return {
        "tipo_servicio": tipo,
        "tiempo_estimado": tiempo
    }

@app.get("/test-bridge")
def probar_bridge(tipo: str, canal: str):

    # Selección del canal
    if canal == "email":
        canal_obj = Email()
    elif canal == "sms":
        canal_obj = SMS()
    else:
        return {"error": "Canal no válido"}

    # Selección del tipo de notificación
    if tipo == "viaje":
        notificacion = NotificacionViaje(canal_obj)
        notificacion.enviar_inicio()

    elif tipo == "emergencia":
        notificacion = NotificacionEmergencia(canal_obj)
        notificacion.enviar_alerta()

    else:
        return {"error": "Tipo no válido"}

    return {
        "tipo": tipo,
        "canal": canal,
        "mensaje": "Notificación enviada"
    }

@app.get("/test-decorator")
def probar_decorator():

    tarifa = TarifaBase(10000)

    # Aplicar decoradores dinámicamente
    tarifa = Peaje(tarifa)
    tarifa = Nocturno(tarifa)
    tarifa = Seguro(tarifa)

    total = tarifa.calcular()

    return {
        "total": total
    }

@app.get("/test-facade")
def probar_facade():

    viaje = {
        "id": 1,
        "total": 20000
    }

    facade = FacadeFinalizarViaje()

    resultado = facade.finalizar_viaje(viaje)

    return resultado

@app.get("/test-composite")
def probar_composite():

    # Servicios individuales
    viaje = ServicioIndividual("Viaje base", 10000)
    seguro = ServicioIndividual("Seguro", 2000)
    peaje = ServicioIndividual("Peaje", 3000)

    # Crear paquete
    paquete = PaqueteServicios("Paquete completo")

    paquete.agregar(viaje)
    paquete.agregar(seguro)
    paquete.agregar(peaje)

    total = paquete.calcular_costo()

    return {
        "total": total
    }