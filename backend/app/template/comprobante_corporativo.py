from app.template.generador_comprobante import (
    GeneradorComprobante
)


class ComprobanteCorporativo(
    GeneradorComprobante
):

    def agregar_extra(self, servicio):

        return (
            "Facturación empresarial "
            "con NIT"
        )