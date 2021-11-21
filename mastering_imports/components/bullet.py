from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_string('''
<Bullet>:
    canvas.after:
        Color:
            rgba: 1, 0, 0, 0.5
        Rectangle:
            pos: root.pos
            size: root.size
            size: 10, 100
''')


class Bullet(Widget):
    def __init__(self, x, **kwargs):
        super().__init__(**kwargs)
        self.x = x

    def move(self):
        self.y += 10
