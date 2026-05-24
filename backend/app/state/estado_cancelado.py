from app.state.estado_servicio import EstadoServicio


class EstadoCancelado(EstadoServicio):

    def aceptar(self, servicio):

        raise Exception(
            "Servicio cancelado"
        )

    def cancelar(self, servicio):

        raise Exception(
            "Servicio ya cancelado"
        )

    def finalizar(self, servicio):

        raise Exception(
            "Servicio cancelado"
        )