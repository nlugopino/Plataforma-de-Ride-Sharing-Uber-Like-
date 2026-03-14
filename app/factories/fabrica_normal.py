from factories.abstract_factory import FabricaAbstractaViaje
from services.tarifa_normal import TarifaNormal

class FabricaViajeNormal(FabricaAbstractaViaje):

    def crear_servicio_tarifa(self, propina=None, descuento=None):
        return TarifaNormal(propina, descuento)