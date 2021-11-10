from random import randint

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty
from kivy.clock import Clock


class MyApp(App):
    def build(self):
        ob = WarZone()
        ob.add_widget(Gun())
        ob.add_widget(GunAdministrator())
        Clock.schedule_interval(ob.update, 1 / 60)
        Clock.schedule_interval(ob.spawn_enemy, 2)
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
