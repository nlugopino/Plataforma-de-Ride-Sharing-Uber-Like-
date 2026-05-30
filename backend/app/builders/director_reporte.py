class DirectorReporte:

    def __init__(
        self,
        builder
    ):
        self.builder = builder

    def construir(self):

        self.builder.agregar_titulo()

        self.builder.agregar_conductor()

        self.builder.agregar_servicios()

        self.builder.agregar_totales()

        return (
            self.builder.obtener_pdf()
        )