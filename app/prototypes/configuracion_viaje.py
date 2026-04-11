import copy
from prototypes.prototype_viaje import PrototypeViaje

# Clase que se va a clonar
class ConfiguracionViaje(PrototypeViaje):

    def __init__(self, tipo, seguridad, trafico, prioridad):
        self.tipo = tipo
        self.seguridad = seguridad
        self.trafico = trafico
        self.prioridad = prioridad

    def clonar(self):
        print("[Prototype] Clonando configuración de viaje")
        return copy.deepcopy(self)

    def mostrar(self):
        return {
            "tipo": self.tipo,
            "seguridad": self.seguridad,
            "trafico": self.trafico,
            "prioridad": self.prioridad
        }