from app.template.generador_comprobante import (
    GeneradorComprobante
)


class ComprobantePremium(
    GeneradorComprobante
):

    def agregar_extra(self, servicio):

        return (
            "Servicio prioritario "
            "y atención preferencial"
        )