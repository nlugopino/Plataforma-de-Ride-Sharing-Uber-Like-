from bridge.notificacion import Notificacion

class NotificacionViaje(Notificacion):

    def enviar_inicio(self):
        self.canal.enviar("Tu viaje ha iniciado")

    def enviar_fin(self):
        self.canal.enviar("Tu viaje ha finalizado")