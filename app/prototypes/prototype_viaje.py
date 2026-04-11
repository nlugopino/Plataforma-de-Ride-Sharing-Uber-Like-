from abc import ABC, abstractmethod
import copy

# Prototype abstracto
class PrototypeViaje(ABC):

    @abstractmethod
    def clonar(self):
        pass