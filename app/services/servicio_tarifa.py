from abc import ABC, abstractmethod

# Clase abstracta que define el comportamiento del cálculo de tarifas
class ServicioTarifa(ABC):

    @abstractmethod
    def calcular_tarifa(self, distancia_km: float):
        pass