from abc import ABC, abstractmethod


class Handler(ABC):

    def __init__(self):

        self.next_handler = None

    def set_next(self, handler):

        self.next_handler = handler

        return handler

    @abstractmethod
    def handle(self, data, db):
        pass