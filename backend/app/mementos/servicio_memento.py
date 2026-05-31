class ServicioMemento:

    def __init__(
        self,
        direccion_origen,
        direccion_destino,
        tipo_servicio,
        distancia_km,
        valor_oferta
    ):

        self.direccion_origen = direccion_origen

        self.direccion_destino = direccion_destino

        self.tipo_servicio = tipo_servicio

        self.distancia_km = distancia_km

        self.valor_oferta = valor_oferta