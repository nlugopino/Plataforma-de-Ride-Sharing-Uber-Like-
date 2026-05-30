from abc import ABC, abstractmethod


class ReporteConductorBuilder(ABC):

    @abstractmethod
    def agregar_titulo(self):
        pass

    @abstractmethod
    def agregar_conductor(self):
        pass

    @abstractmethod
    def agregar_servicios(self):
        pass

    @abstractmethod
    def agregar_totales(self):
        pass

    @abstractmethod
    def obtener_pdf(self):
        pass