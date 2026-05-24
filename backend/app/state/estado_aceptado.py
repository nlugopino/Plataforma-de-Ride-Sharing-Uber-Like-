from app.state.estado_servicio import EstadoServicio


class EstadoAceptado(EstadoServicio):

    def aceptar(self, servicio):

        raise Exception(
            "El servicio ya fue aceptado"
        )

    def cancelar(self, servicio):

        raise Exception(
            "No se puede cancelar un servicio aceptado"
        )

    def finalizar(self, servicio):

        servicio.estado = "finalizado"