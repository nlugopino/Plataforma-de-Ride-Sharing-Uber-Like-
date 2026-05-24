class ProcesadorPago:

    def __init__(self, strategy):

        self.strategy = strategy

    def procesar(self, monto):

        return self.strategy.pagar(monto)