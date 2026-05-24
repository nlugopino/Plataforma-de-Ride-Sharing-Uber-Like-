from app.command.command import Command


class UbicacionCommand(Command):

    def __init__(self, receiver):

        self.receiver = receiver

    def execute(self):

        return self.receiver.compartir()