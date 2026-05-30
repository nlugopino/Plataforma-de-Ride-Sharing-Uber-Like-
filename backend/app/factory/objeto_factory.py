from abc import ABC


class ObjetoPerdidoBase(ABC):

    def __init__(
        self,
        descripcion
    ):
        self.descripcion = descripcion