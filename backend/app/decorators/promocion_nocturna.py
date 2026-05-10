from app.decorators.decorator_base import DecoradorTarifa


class PromocionNocturna(DecoradorTarifa):

    def calcular(self):

        costo = self.tarifa.calcular()

        descuento = costo * 0.08

        return costo - descuento