from app.services.factory.servicio_base import ServicioBase


class ServicioPedido(ServicioBase):

    def descripcion(self):
        return "Servicio de pedido"