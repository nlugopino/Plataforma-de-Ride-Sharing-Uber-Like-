from factories.abstract_factory import FabricaAbstractaViaje
from services.tarifa_premium import TarifaPremium

class FabricaViajePremium(FabricaAbstractaViaje):

    def crear_servicio_tarifa(self, propina=None, descuento=None):

        print("🟣 [Abstract Factory] Creando servicio de tarifa PREMIUM")

        return TarifaPremium(propina, descuento)