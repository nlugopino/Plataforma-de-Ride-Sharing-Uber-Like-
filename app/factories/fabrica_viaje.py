from models.viaje import Viaje
from services.servicio_tarifa import ServicioTarifa

# Patrón Factory Method - ¿Qué problema resuelve?
# Crear un viaje implica: Calcular el precio, Crear el objeto, En el futuro: decidir tipo de viaje
# Centraliza la creación de objetos, Oculta la complejidad, Permite extender sin modificar

class FabricaViaje:

    @staticmethod
    def crear_viaje(distancia_km: float) -> Viaje:
        # Se crea el servicio encargado de calcular la tarifa
        servicio_tarifa = ServicioTarifa()
        # Se calcula la tarifa del viaje
        tarifa = servicio_tarifa.calcular_tarifa(distancia_km)
        # Se crea y retorna el objeto Viaje
        return Viaje(distancia_km, tarifa)