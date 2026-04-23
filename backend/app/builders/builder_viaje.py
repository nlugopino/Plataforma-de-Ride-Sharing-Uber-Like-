from abc import ABC, abstractmethod

class BuilderViaje(ABC):
# Esta clase define los pasos necesarios para construir un objeto Viaje.
# Cada método representa una parte del proceso de construcción.

    @abstractmethod
    def agregar_distancia(self, distancia):
        pass

    @abstractmethod
    def agregar_tarifa(self, tarifa):
        pass

    @abstractmethod
    def agregar_propina(self, propina):
        pass

    @abstractmethod
    def construir(self):
        pass