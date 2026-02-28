from core.configuracion import ConfiguracionApp

# Servicio encargado de la lógica de cálculo de tarifas
class ServicioTarifa:

    def calcular_tarifa(self, distancia_km: float) -> float:
        # Se obtiene la configuración global (Singleton)
        configuracion = ConfiguracionApp()
        # Cálculo de la tarifa usando valores compartidos
        return configuracion.tarifa_base + (
            distancia_km * configuracion.precio_por_km
        )