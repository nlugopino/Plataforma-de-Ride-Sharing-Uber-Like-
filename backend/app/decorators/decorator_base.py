from app.decorators.interfaz_tarifa import InterfazTarifa

# Decorador base
class DecoradorTarifa(InterfazTarifa):

    def __init__(self, tarifa):
        self.tarifa = tarifa

    def calcular(self):
        return self.tarifa.calcular()