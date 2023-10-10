from abc import ABC, abstractmethod


class Buttom(ABC):

    @abstractmethod
    def paint():
        pass


class WinButtom(Buttom):

    def paint():
        pass


class MacButtom(Buttom):

    def paint():
        pass
