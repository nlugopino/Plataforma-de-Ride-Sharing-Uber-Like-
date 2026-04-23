from app.builders.builder_viaje import BuilderViaje
from app.models.viaje import Viaje

class ViajeBuilder(BuilderViaje):

    def __init__(self):
        print("🔵 [Builder] Iniciando construcción del objeto Viaje")
        self.viaje = Viaje()

    def agregar_distancia(self, distancia):
        print(f"🔵 [Builder] Agregando distancia: {distancia}")
        self.viaje.distancia = distancia
        return self

    def agregar_tarifa(self, tarifa):
        print(f"🔵 [Builder] Agregando tarifa base: {tarifa}")
        self.viaje.tarifa = tarifa
        return self

    def agregar_propina(self, propina):
        print(f"🔵 [Builder] Agregando propina: {propina}")
        self.viaje.propina = propina if propina else 0
        return self

    def construir(self):

        print("🔵 [Builder] Finalizando construcción del viaje")

        self.viaje.total = self.viaje.tarifa + self.viaje.propina

        return self.viaje