from app.state.estado_pendiente import EstadoPendiente
from app.state.estado_aceptado import EstadoAceptado
from app.state.estado_finalizado import EstadoFinalizado
from app.state.estado_cancelado import EstadoCancelado


class ServicioContext:

    def __init__(self, servicio):

        self.servicio = servicio

        self.estado = self.obtener_estado()

    def obtener_estado(self):

        if self.servicio.estado == "pendiente":
            return EstadoPendiente()

        elif self.servicio.estado == "aceptado":
            return EstadoAceptado()

        elif self.servicio.estado == "finalizado":
            return EstadoFinalizado()

        elif self.servicio.estado == "cancelado":
            return EstadoCancelado()

    def aceptar(self):

        self.estado.aceptar(self.servicio)

    def cancelar(self):

        self.estado.cancelar(self.servicio)

    def finalizar(self):

        self.estado.finalizar(self.servicio)