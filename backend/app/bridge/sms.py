from app.bridge.canal_notificacion import CanalNotificacion

class SMS(CanalNotificacion):

    def enviar(self, mensaje):
        print(f"[Bridge] Enviando SMS: {mensaje}")