from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, StringProperty
from kivy.clock import Clock
from random import random, randint

Builder.load_string('''
<Result>:
    canvas:
        Color:
            rgba: 0, 0, 0, 0.8
        Rectangle:
            size: 700, 700 # TODO: Get the window size.
    Label:
        text: root.text
        pos: 350, 350
    Button:
        text: 'P L A Y   A G A I N'
        size: 200, 100
        pos: 300, 200
        on_press: root.play_again()
''')


class Result(Widget):
    text = StringProperty()

    def __init__(self, WZ, text, **kwargs):
        super().__init__(**kwargs)
        self.WZ = WZ
        self.text = text

    def play_again(self):
        self.WZ.restart()


class MyApp(App):
    def build(self):
        ob = Result('L O S E R')
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
