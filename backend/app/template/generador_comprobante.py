from abc import ABC, abstractmethod


class GeneradorComprobante(ABC):

    def generar(self, servicio):

        datos = self.obtener_datos(servicio)

        total = self.calcular_total(servicio)

        extra = self.agregar_extra(servicio)

        return {
            "datos": datos,
            "total": total,
            "extra": extra
        }

    def obtener_datos(self, servicio):

        return {
            "origen": servicio.direccion_origen,
            "destino": servicio.direccion_destino
        }

    def calcular_total(self, servicio):

        return servicio.total_final

    @abstractmethod
    def agregar_extra(self, servicio):
        pass