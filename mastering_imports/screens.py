from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, StringProperty
from kivy.clock import Clock
from random import random, randint

from mastering_imports.gun_administrator import GunAdministrator
from mastering_imports.info_display import Info
from mastering_imports.objects import Gun
from mastering_imports.war_zone import WarZone

Builder.load_string('''
<MainGUI>:
    
''')


class MainGUI(Widget):
    ob = WarZone()
    ob.add_widget(Gun(ob))
    ob.add_widget(GunAdministrator(ob))
    ob.add_widget(Info(ob))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(self.ob)


class MyApp(App):
    def build(self):
        ob = MainGUI()
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
