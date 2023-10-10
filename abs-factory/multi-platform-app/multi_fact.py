from abc import ABC, abstractmethod
from multi_plat_button import Button
from multi_plat_checkbox import Checkbox


class GUIFactory(ABC):

    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass


class WinFactory(GUIFactory):

    def createButton(self) -> Button:
        return Button

    def createCheckbox(self) -> Checkbox:
        return Checkbox


class MacFactory(GUIFactory):

    def createButton(self) -> Button:
        return Button

    def createCheckbox(self) -> Checkbox:
        return Checkbox
