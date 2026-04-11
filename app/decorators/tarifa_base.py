from decorators.interfaz_tarifa import InterfazTarifa

class TarifaBase(InterfazTarifa):

    def __init__(self, costo):
        self.costo = costo

    def calcular(self):
        print("[Decorator] Tarifa base:", self.costo)
        return self.costo