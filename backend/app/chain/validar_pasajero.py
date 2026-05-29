from app.chain.handler import Handler
from app.models.pasajero import Pasajero


class ValidarPasajero(Handler):

    def handle(self, data, db):

        pasajero = db.query(
            Pasajero
        ).first()

        if not pasajero:

            raise Exception(
                "No existe pasajero registrado"
            )

        if self.next_handler:

            return self.next_handler.handle(
                data,
                db
            )

        return True