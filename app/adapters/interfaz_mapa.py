from abc import ABC, abstractmethod

# Interfaz estándar del sistema
class InterfazMapa(ABC):

    @abstractmethod
    def obtener_tiempo(self, origen, destino):
        pass