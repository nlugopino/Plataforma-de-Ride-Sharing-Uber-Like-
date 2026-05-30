from app.decorators.decorator_base import DecoradorTarifa


class Propina(DecoradorTarifa):

    def __init__(
        self,
        tarifa,
        valor_propina
    ):
        super().__init__(tarifa)

        self.valor_propina = valor_propina

    def calcular(self):

        costo = self.tarifa.calcular()

        return costo + self.valor_propina