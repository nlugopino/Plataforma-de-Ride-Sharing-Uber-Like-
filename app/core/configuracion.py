# Patrón Singleton
# Esta clase garantiza que solo exista UNA instancia de configuración
# para toda la aplicación. Así todos los servicios usan los mismos valores.

class ConfiguracionApp:

    _instancia = None

    def __new__(cls):

        # Si no existe instancia, se crea
        if cls._instancia is None:
            print("🔴 [Singleton] Creando instancia única de ConfiguracionApp")

            cls._instancia = super(ConfiguracionApp, cls).__new__(cls)

            # Valores compartidos en toda la aplicación
            cls._instancia.tarifa_base = 5000
            cls._instancia.precio_por_km = 2000

        else:
            print("🔴 [Singleton] Reutilizando instancia existente de ConfiguracionApp")

        return cls._instancia