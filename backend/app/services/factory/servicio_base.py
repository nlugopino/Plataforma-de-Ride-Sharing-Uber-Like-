from abc import ABC, abstractmethod


class ServicioBase(ABC):

    @abstractmethod
    def descripcion(self):
        pass