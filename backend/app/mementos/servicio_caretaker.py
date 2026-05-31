class ServicioCaretaker:

    ultimo_memento = None

    @classmethod
    def guardar(
        cls,
        memento
    ):
        cls.ultimo_memento = memento

    @classmethod
    def obtener(
        cls
    ):
        return cls.ultimo_memento