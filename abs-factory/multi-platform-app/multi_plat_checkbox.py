from abc import ABC, abstractmethod


class Checkbox(ABC):
    @abstractmethod
    def paint():
        pass


class WinCheckbox(Checkbox):
    @abstractmethod
    def paint():
        pass

class MacCheckbox(Checkbox):
    @abstractmethod
    def paint():
        pass
