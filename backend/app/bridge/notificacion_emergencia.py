from app.bridge.notificacion import Notificacion

class NotificacionEmergencia(Notificacion):

    def enviar_alerta(self):
        self.canal.enviar("Emergencia detectada en el viaje")