from app.observer.observer import Observer


class NotificacionObserver(Observer):

    def __init__(self):
        self.ultima_notificacion = None

    def update(self, mensaje):

        print(f"[Observer] {mensaje}")

        self.ultima_notificacion = mensaje