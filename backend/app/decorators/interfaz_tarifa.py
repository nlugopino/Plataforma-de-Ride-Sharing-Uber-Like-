from abc import ABC, abstractmethod

# Componente base
class InterfazTarifa(ABC):

    @abstractmethod
    def calcular(self):
        pass