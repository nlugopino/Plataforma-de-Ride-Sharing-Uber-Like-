from facade.servicio_pago import ServicioPago
from facade.servicio_historial import ServicioHistorial
from facade.servicio_notificacion import ServicioNotificacion

# Facade
class FacadeFinalizarViaje:

    def __init__(self):
        self.pago = ServicioPago()
        self.historial = ServicioHistorial()
        self.notificacion = ServicioNotificacion()

    def finalizar_viaje(self, viaje):

        print("[Facade] Iniciando proceso de finalización del viaje")

        # 1. Procesar pago
        self.pago.procesar_pago(viaje["total"])

        # 2. Guardar historial
        self.historial.guardar_viaje(viaje)

        # 3. Notificar usuario
        self.notificacion.enviar("Tu viaje ha finalizado correctamente")

        print("[Facade] Proceso completado")

        return {"estado": "viaje finalizado"}