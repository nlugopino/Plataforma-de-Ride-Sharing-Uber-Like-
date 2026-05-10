class NivelBuilder:

    def construir(self, puntos):

        nivel = "Bronce"

        beneficio = "Sin beneficios"

        if puntos >= 100:

            nivel = "Oro"

            beneficio = "Viajes prioritarios"

        elif puntos >= 50:

            nivel = "Plata"

            beneficio = "5% descuento"

        return {
            "nivel": nivel,
            "beneficio": beneficio
        }