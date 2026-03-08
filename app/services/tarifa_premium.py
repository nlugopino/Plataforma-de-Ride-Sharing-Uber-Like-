from services.servicio_tarifa import ServicioTarifa

class TarifaPremium(ServicioTarifa):

    def calcular_tarifa(self, distancia_km: float):
        return 8000 + (distancia_km * 3000)