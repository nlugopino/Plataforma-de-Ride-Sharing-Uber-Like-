from app.services.factory.servicio_viaje import ServicioViaje
from app.services.factory.servicio_pedido import ServicioPedido
from app.services.factory.servicio_mensajeria import ServicioMensajeria


class ServicioFactory:

    @staticmethod
    def crear(tipo):

        if tipo == "viaje":
            return ServicioViaje()

        elif tipo == "pedido":
            return ServicioPedido()

        elif tipo == "mensajeria":
            return ServicioMensajeria()

        else:
            raise Exception("Tipo inválido")