from app.adapters.interfaz_mapa import InterfazMapa
from app.adapters.servicio_externo_a import ServicioMapaA

# Adapter para Servicio A
class AdapterMapaA(InterfazMapa):

    def __init__(self):
        self.servicio = ServicioMapaA()

    def obtener_tiempo(self, origen, destino):

        print("🔵 [Adapter] Usando ServicioMapaA")

        resultado = self.servicio.calcular_ruta(origen, destino)

        # Adaptación del formato
        return resultado["tiempo_minutos"]