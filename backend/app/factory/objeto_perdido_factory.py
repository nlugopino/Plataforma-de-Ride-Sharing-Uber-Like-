from app.factory.celular import (
    CelularPerdido
)

from app.factory.llaves import (
    LlavesPerdidas
)

from app.factory.billetera import (
    BilleteraPerdida
)


class ObjetoPerdidoFactory:

    @staticmethod
    def crear(
        tipo,
        descripcion
    ):

        if tipo == "celular":
            return CelularPerdido(
                descripcion
            )

        if tipo == "llaves":
            return LlavesPerdidas(
                descripcion
            )

        if tipo == "billetera":
            return BilleteraPerdida(
                descripcion
            )

        return CelularPerdido(
            descripcion
        )