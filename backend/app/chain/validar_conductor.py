from app.chain.handler import Handler
from app.models.conductor import Conductor


class ValidarConductor(Handler):

    def handle(self, data, db):

        conductor = db.query(
            Conductor
        ).first()

        if not conductor:

            raise Exception(
                "No existe conductor registrado"
            )

        if self.next_handler:

            return self.next_handler.handle(
                data,
                db
            )

        return True