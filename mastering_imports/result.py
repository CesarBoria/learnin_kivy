from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, StringProperty

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
    Label:
        text: "Next round's speed:"
        pos: 250, 100
    Label:
        text: root.speed
        pos: 450, 100
    Button:
        text: 'P L A Y   A G A I N'
        size: 200, 100
        pos: 300, 200
        on_press: root.play_again()
''')


class Result(Widget):
    text = StringProperty()
    speed = StringProperty()

    def __init__(self, WZ, text, speed, **kwargs):
        super().__init__(**kwargs)
        self.WZ = WZ
        self.text = text
        self.speed = str(round(speed * 100))

    def play_again(self):
        self.WZ.restart()


class MyApp(App):
    def build(self):
        ob = Result('L O S E R')
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
