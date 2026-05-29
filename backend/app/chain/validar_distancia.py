from app.chain.handler import Handler


class ValidarDistancia(Handler):

    def handle(self, data, db):

        if data.distancia_km <= 0:

            raise Exception(
                "La distancia debe ser mayor a cero"
            )

        if self.next_handler:

            return self.next_handler.handle(
                data,
                db
            )

        return True