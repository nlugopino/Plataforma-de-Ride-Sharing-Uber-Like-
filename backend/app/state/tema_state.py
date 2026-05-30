from abc import ABC, abstractmethod


class TemaState(ABC):

    @abstractmethod
    def nombre(self):
        pass