from app.template.generador_comprobante import (
    GeneradorComprobante
)


class ComprobanteEstandar(
    GeneradorComprobante
):

    def agregar_extra(self, servicio):

        return "Comprobante estándar"