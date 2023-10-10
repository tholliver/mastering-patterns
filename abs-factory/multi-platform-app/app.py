from multi_plat_button import Button
from multi_plat_checkbox import Checkbox
from multi_fact import GUIFactory
import random
from multi_fact import WinFactory, MacFactory


class Application:
    _buttom: Button

    def __init__(self, factory: GUIFactory) -> None:
        self.factory = factory

    def createUI(self):
        self._buttom = self.factory.createButton()
        return self._buttom

    def paint(self):
        self._buttom.paint()


class ApplicationConfigurator:
    factory = None

    def main(self):
        config = self.readApplicationConfigFile()

        if config == 'win':
            self.factory = WinFactory()
        elif config == 'mac':
            self.factory = MacFactory()
        else:
            Exception("Error unknown")

        app = Application(self.factory)
        print('App initialized: ', app.createUI(),
              'type button to render', type(app.createUI()))

    def readApplicationConfigFile(self) -> str:
        file_sys = 'win' if random.random() > 0.50 else 'mac'
        print(f'Reading file for {file_sys} config...')
        return file_sys


if __name__ == '__main__':
    ""
    conApp = ApplicationConfigurator()
    conApp.main()
