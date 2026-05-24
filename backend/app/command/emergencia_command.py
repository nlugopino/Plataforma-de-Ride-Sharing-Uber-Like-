from app.command.command import Command


class EmergenciaCommand(Command):

    def __init__(self, receiver):

        self.receiver = receiver

    def execute(self):

        return self.receiver.activar()