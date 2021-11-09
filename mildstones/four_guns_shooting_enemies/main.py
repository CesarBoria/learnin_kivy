from kivy.config import Config

# Config.set('graphics', 'width', 380)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from test import ThingWidget
from info_display import InfoArea
from war_zone import WarZone
from gun_module import GunWidget

from kivy.lang.builder import Builder

Builder.load_string('''
#:include info_display.kv
#:include war_zone.kv
#:include gun_module.kv

<MainWidget>:
    orientation: 'vertical'
    # InfoArea:
    #     size_hint_y: 0.1
    # WarZone:
    #     size_hint_y: 0.6
    # GunWidget:
    #     size_hint_y: 0.3
''')


class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.add_widget(GunWidget())
        self.add_widget(ThingWidget())


class ZoombiesApp(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    app_instance = ZoombiesApp()
    app_instance.run()
