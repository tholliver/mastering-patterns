from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def paint() -> None:
        pass


class WinButtom(Button):

    def paint():
        pass


class MacButtom(Button):

    def paint():
        pass
