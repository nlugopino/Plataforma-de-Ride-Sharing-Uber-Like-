from decorators.decorator_base import DecoradorTarifa

class Seguro(DecoradorTarifa):

    def calcular(self):
        costo = self.tarifa.calcular()
        print("[Decorator] Seguro adicional: 1500")
        return costo + 1500