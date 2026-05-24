from datetime import datetime
from app.state.servicio_context import ServicioContext
from app.decorators.tarifa_base import TarifaBase
from app.decorators.promocion_primer_viaje import PromocionPrimerViaje
from app.decorators.promocion_fin_semana import PromocionFinSemana
from app.decorators.promocion_nocturna import PromocionNocturna
from app.models.servicio import Servicio
from app.models.pasajero import Pasajero
from app.builders.nivel_builder import NivelBuilder
from app.observer.servicio_subject import ServicioSubject
from app.observer.notificacion_observer import NotificacionObserver
from app.strategy.pago_efectivo import PagoEfectivo
from app.strategy.pago_tarjeta import PagoTarjeta
from app.strategy.pago_wallet import PagoWallet
from app.strategy.procesador_pago import ProcesadorPago

class FacadeServicio:

    nivel_builder = NivelBuilder()

    subject = ServicioSubject()

    observer = NotificacionObserver()

    subject.attach(observer)

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
            pasajero_id=pasajero_id,
            metodo_pago=data.metodo_pago
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

        context = ServicioContext(servicio)

        context.aceptar()

        servicio.conductor_id = conductor_id

        db.commit()

        db.refresh(servicio)

        self.subject.notify(
            "Tu viaje fue aceptado"
        )

        return servicio

    def finalizar(
        self,
        db,
        servicio
    ):
        
        strategy = None

        if servicio.metodo_pago == "efectivo":
            strategy = PagoEfectivo()

        elif servicio.metodo_pago == "tarjeta":
            strategy = PagoTarjeta()

        elif servicio.metodo_pago == "wallet":
            strategy = PagoWallet()

        procesador = ProcesadorPago(strategy)

        resultado_pago = procesador.procesar(
            servicio.total_final
        )

        print(resultado_pago)

        context = ServicioContext(servicio)

        context.finalizar()

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

        self.subject.notify(
            "Tu viaje finalizó correctamente"
        )

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

        context = ServicioContext(servicio)

        context.cancelar()

        db.commit()

        db.refresh(servicio)

        self.subject.notify(
            "El viaje fue cancelado"
        )

        return servicio