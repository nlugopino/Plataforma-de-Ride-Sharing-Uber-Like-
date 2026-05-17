class ServicioSubject:

    def __init__(self):

        self.observers = []

    def attach(self, observer):

        self.observers.append(observer)

    def notify(self, mensaje):

        for observer in self.observers:

            observer.update(mensaje)