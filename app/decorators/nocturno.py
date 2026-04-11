from decorators.decorator_base import DecoradorTarifa

class Nocturno(DecoradorTarifa):

    def calcular(self):
        costo = self.tarifa.calcular()
        print("[Decorator] Recargo nocturno: 2000")
        return costo + 2000