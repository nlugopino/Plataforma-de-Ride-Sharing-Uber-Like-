from app.strategy.payment_strategy import PaymentStrategy


class PagoTarjeta(PaymentStrategy):

    def pagar(self, monto):

        return f"Pago con tarjeta por ${monto}"