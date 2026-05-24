from app.state.estado_servicio import EstadoServicio


class EstadoPendiente(EstadoServicio):

    def aceptar(self, servicio):

        servicio.estado = "aceptado"

    def cancelar(self, servicio):

        servicio.estado = "cancelado"

    def finalizar(self, servicio):

        raise Exception(
            "No se puede finalizar un servicio pendiente"
        )