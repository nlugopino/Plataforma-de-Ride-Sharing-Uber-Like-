from decorators.decorator_base import DecoradorTarifa

class Peaje(DecoradorTarifa):

    def calcular(self):
        costo = self.tarifa.calcular()
        print("[Decorator] Agregando peaje: 3000")
        return costo + 3000