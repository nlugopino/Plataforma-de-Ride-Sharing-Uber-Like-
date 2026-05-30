from pydantic import BaseModel


class ObjetoPerdidoRequest(
    BaseModel
):

    tipo: str

    descripcion: str