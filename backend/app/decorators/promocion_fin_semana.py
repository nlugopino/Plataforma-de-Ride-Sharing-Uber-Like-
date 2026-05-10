from app.decorators.decorator_base import DecoradorTarifa


class PromocionFinSemana(DecoradorTarifa):

    def calcular(self):

        costo = self.tarifa.calcular()

        descuento = costo * 0.05

        return costo - descuento