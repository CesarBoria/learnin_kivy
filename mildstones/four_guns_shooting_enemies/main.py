from kivy.config import Config

Config.set('graphics', 'width', 380)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

from info_display import InfoArea
from war_zone import WarZone
from input_area import InputArea


class MainWidget(BoxLayout):
    pass


class ZoombiesApp(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    app_instance = ZoombiesApp()
    app_instance.run()
