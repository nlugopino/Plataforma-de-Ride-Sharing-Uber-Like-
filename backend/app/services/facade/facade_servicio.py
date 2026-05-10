from datetime import datetime
from app.decorators.tarifa_base import TarifaBase
from app.decorators.promocion_primer_viaje import PromocionPrimerViaje
from app.decorators.promocion_fin_semana import PromocionFinSemana
from app.decorators.promocion_nocturna import PromocionNocturna
from app.models.servicio import Servicio
from app.models.pasajero import Pasajero
from app.builders.nivel_builder import NivelBuilder

class FacadeServicio:

    nivel_builder = NivelBuilder()

    def solicitar(
        self,
        db,
        data,
        pasajero_id
    ):

        tarifa = TarifaBase(data.valor_oferta)

        promociones_activas = []

        valor_original = data.valor_oferta

        ahora = datetime.now()

        # =========================
        # PRIMER VIAJE
        # =========================

        viajes_finalizados = db.query(Servicio).filter(
            Servicio.pasajero_id == pasajero_id,
            Servicio.estado == "finalizado"
        ).count()

        if viajes_finalizados == 0:

            tarifa = PromocionPrimerViaje(tarifa)

            promociones_activas.append(
                "🎁 Primer viaje -10%"
            )

        # =========================
        # FIN DE SEMANA
        # =========================

        if ahora.weekday() == 5:

            tarifa = PromocionFinSemana(tarifa)

            promociones_activas.append(
                "🔥 Fin de semana -5%"
            )

        # =========================
        # NOCTURNA
        # =========================

        if (
            ahora.weekday() in [0, 1, 2]
            and
            18 <= ahora.hour <= 22
        ):

            tarifa = PromocionNocturna(tarifa)

            promociones_activas.append(
                "🌙 Promo nocturna -8%"
            )

        total_final = tarifa.calcular()

        descuento = valor_original - total_final

        servicio = Servicio(

            direccion_origen=data.direccion_origen,

            direccion_destino=data.direccion_destino,

            tipo_servicio=data.tipo_servicio,

            distancia_km=data.distancia_km,

            valor_oferta=data.valor_oferta,

            descuento_aplicado=descuento,

            promociones=", ".join(promociones_activas),

            total_final=total_final,

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

        pasajero = db.query(Pasajero).filter(
            Pasajero.id == servicio.pasajero_id
        ).first()

        puntos_ganados = int(
            servicio.total_final / 1000
        )

        pasajero.puntos += puntos_ganados

        nivel_data = self.nivel_builder.construir(
            pasajero.puntos
        )

        pasajero.nivel = nivel_data["nivel"]

        db.commit()

        db.refresh(servicio)

        return {
            "mensaje": "Servicio finalizado",
            "puntos_ganados": puntos_ganados,
            "nivel": pasajero.nivel
        }

    def cancelar(
        self,
        db,
        servicio
    ):

        servicio.estado = "cancelado"

        db.commit()

        db.refresh(servicio)

        return servicio