class ReputacionDecorator:

    def agregar_calificacion(
        self,
        servicio,
        calificacion,
        comentario
    ):

        servicio.calificacion = calificacion
        servicio.comentario_calificacion = comentario

        return servicio