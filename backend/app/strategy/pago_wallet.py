from app.strategy.payment_strategy import PaymentStrategy


class PagoWallet(PaymentStrategy):

    def pagar(self, monto):

        return f"Pago con wallet por ${monto}"