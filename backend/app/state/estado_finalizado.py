from app.state.estado_servicio import EstadoServicio


class EstadoFinalizado(EstadoServicio):

    def aceptar(self, servicio):

        raise Exception(
            "Servicio finalizado"
        )

    def cancelar(self, servicio):

        raise Exception(
            "Servicio finalizado"
        )

    def finalizar(self, servicio):

        raise Exception(
            "Servicio ya finalizado"
        )