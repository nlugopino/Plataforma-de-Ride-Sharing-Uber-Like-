from app.factories.abstract_factory import FabricaAbstractaViaje
from app.services.tarifa_normal import TarifaNormal

class FabricaViajeNormal(FabricaAbstractaViaje):

    def crear_servicio_tarifa(self, propina=None, descuento=None):

        print("🟢 [Abstract Factory] Creando servicio de tarifa NORMAL")

        return TarifaNormal(propina, descuento)