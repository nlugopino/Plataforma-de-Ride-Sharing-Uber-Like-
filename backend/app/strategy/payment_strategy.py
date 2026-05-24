from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pagar(self, monto):
        pass