from abc import ABC, abstractmethod

# Componente base
class ComponenteServicio(ABC):

    @abstractmethod
    def calcular_costo(self):
        pass