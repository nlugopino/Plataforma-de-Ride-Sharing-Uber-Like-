from abc import ABC, abstractmethod
from typing import Optional

# Fábrica abstracta que define cómo crear servicios de tarifa
class FabricaAbstractaViaje(ABC):

    @abstractmethod
    def crear_servicio_tarifa(
        self,
        propina: Optional[float] = None,
        descuento: Optional[float] = None
    ):
        pass