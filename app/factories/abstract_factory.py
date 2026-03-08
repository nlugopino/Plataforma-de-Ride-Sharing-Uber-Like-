from abc import ABC, abstractmethod

class FabricaAbstractaViaje(ABC):

    @abstractmethod
    def crear_servicio_tarifa(self):
        pass