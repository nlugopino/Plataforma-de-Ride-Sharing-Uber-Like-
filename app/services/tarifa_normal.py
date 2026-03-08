from services.servicio_tarifa import ServicioTarifa

class TarifaNormal(ServicioTarifa):

    def calcular_tarifa(self, distancia_km: float):
        return 5000 + (distancia_km * 2000)