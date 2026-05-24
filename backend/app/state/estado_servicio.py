from abc import ABC, abstractmethod


class EstadoServicio(ABC):

    @abstractmethod
    def aceptar(self, servicio):
        pass

    @abstractmethod
    def cancelar(self, servicio):
        pass

    @abstractmethod
    def finalizar(self, servicio):
        pass