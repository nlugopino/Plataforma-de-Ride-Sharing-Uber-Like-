from bridge.canal_notificacion import CanalNotificacion

class Email(CanalNotificacion):

    def enviar(self, mensaje):
        print(f"[Bridge] Enviando EMAIL: {mensaje}")