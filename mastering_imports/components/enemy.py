from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.lang.builder import Builder

Builder.load_string('''
<Enemy>:
    size: root.s, root.s
    canvas.after:
        Color:
            rgba: 1, 0, 0, 0.5
        Rectangle:
            pos: root.pos
            size: root.size
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
''')


class Enemy(Widget):
    s = NumericProperty(100)
    walked = 0

    def __init__(self, x, **kwargs):
        super().__init__(**kwargs)
        self.x = x

    def move(self):
        self.y = self.parent.height - 100 - self.walked
        self.walked += 0.5

    def check_collision(self, bullet):
        if self.collide_widget(bullet):
            return True

    def check_conquest(self):
        if self.y < 0:
            return True

    @staticmethod
    def spawn(root, x, *largs):
        if root.state["num_enemies"] > root.state["spawned_enemies"]:
            enemy = Enemy(x)
            root.state["spawned_enemies"] += 1
            root.state["enemies"].append(enemy)
            root.add_widget(enemy)
