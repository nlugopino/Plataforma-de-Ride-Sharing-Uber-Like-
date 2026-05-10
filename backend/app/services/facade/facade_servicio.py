from datetime import datetime

from app.models.servicio import Servicio


class FacadeServicio:

    def solicitar(
        self,
        db,
        data,
        pasajero_id
    ):

        servicio = Servicio(

            direccion_origen=data.direccion_origen,
            direccion_destino=data.direccion_destino,

            tipo_servicio=data.tipo_servicio,

            distancia_km=data.distancia_km,

            valor_oferta=data.valor_oferta,

            pasajero_id=pasajero_id
        )

        db.add(servicio)

        db.commit()

        db.refresh(servicio)

        return servicio

    def aceptar(
        self,
        db,
        servicio,
        conductor_id
    ):

        servicio.estado = "aceptado"

        servicio.conductor_id = conductor_id

        db.commit()

        db.refresh(servicio)

        return servicio

    def finalizar(
        self,
        db,
        servicio
    ):

        servicio.estado = "finalizado"

        servicio.fecha_finalizacion = datetime.utcnow()

        db.commit()

        db.refresh(servicio)

        return servicio

    def cancelar(
        self,
        db,
        servicio
    ):

        servicio.estado = "cancelado"

        db.commit()

        db.refresh(servicio)

        return servicio