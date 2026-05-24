from app.strategy.payment_strategy import PaymentStrategy


class PagoEfectivo(PaymentStrategy):

    def pagar(self, monto):

        return f"Pago en efectivo por ${monto}"