from app.adapters.interfaz_mapa import InterfazMapa
from app.adapters.servicio_externo_b import ServicioMapaB

# Adapter para Servicio B
class AdapterMapaB(InterfazMapa):

    def __init__(self):
        self.servicio = ServicioMapaB()

    def obtener_tiempo(self, origen, destino):

        print("🔵 [Adapter] Usando ServicioMapaB")

        resultado = self.servicio.get_route(origen, destino)

        # Adaptación del formato
        return resultado["duration"]