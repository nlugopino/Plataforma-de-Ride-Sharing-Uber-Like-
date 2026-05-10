from app.decorators.decorator_base import DecoradorTarifa


class PromocionPrimerViaje(DecoradorTarifa):

    def calcular(self):

        costo = self.tarifa.calcular()

        descuento = costo * 0.10

        return costo - descuento