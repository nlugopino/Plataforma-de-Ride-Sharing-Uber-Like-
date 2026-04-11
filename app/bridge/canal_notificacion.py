from abc import ABC, abstractmethod

# Implementación
class CanalNotificacion(ABC):

    @abstractmethod
    def enviar(self, mensaje):
        pass