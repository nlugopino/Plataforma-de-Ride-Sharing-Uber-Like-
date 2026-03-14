from services.servicio_tarifa import ServicioTarifa

class TarifaNormal(ServicioTarifa):

    def __init__(self, propina=None, descuento=None):
        self.propina = propina
        self.descuento = descuento

    def calcular_tarifa(self, distancia_km: float):

        tarifa = 5000 + (distancia_km * 2000)

        if self.descuento:
            tarifa -= self.descuento

        if self.propina:
            tarifa += self.propina

        return tarifa