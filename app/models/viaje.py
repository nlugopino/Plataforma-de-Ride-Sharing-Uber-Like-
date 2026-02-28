# Clase que representa la entidad Viaje del dominio
class Viaje:
    def __init__(self, distancia_km: float, tarifa: float):
        self.distancia_km = distancia_km
        self.tarifa = tarifa