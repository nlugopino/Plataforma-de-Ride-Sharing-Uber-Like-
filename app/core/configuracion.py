# Patrón Singleton - ¿Qué problema resuelve esta clase?
# Hay valores globales como: tarifa base, precio por kilómetro.
# Estos valores no deben duplicarse. Todos los servicios deben usar los mismos datos
class ConfiguracionApp:

    _instancia = None

    def __new__(cls):
        # Si no existe una instancia, se crea por primera vez
        if cls._instancia is None:
            cls._instancia = super(ConfiguracionApp, cls).__new__(cls)
            # Valores de configuración compartidos por todo el sistema
            cls._instancia.tarifa_base = 5000
            cls._instancia.precio_por_km = 2000
        # Siempre se retorna la misma instancia
        return cls._instancia