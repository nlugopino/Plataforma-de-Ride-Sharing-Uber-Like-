from app.chain.handler import Handler


class ValidarOferta(Handler):

    def handle(self, data, db):

        if data.valor_oferta < 5000:

            raise Exception(
                "La oferta mínima es $5000"
            )

        if self.next_handler:

            return self.next_handler.handle(
                data,
                db
            )

        return True