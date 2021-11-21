from random import randint

from kivy.lang.builder import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty, ListProperty

from components.bullet import Bullet

Builder.load_string('''
<GunChulo>:
    Button:
        text: root.operation + '\\n' + root.response
        font_size: 50
        on_release: root.parent.button_clicked(root)
        background_color: root.color
        pos: 100, 0
''')


class GunChulo(RelativeLayout):
    first, second = randint(0, 9), randint(0, 9)
    operator = '+'
    operation = f'{first} {operator} {second}'
    operation_kv = StringProperty(operation)
    result = str(eval(operation))
    response = StringProperty('')
    state = 'OFF'
    color = ListProperty([1 for i in range(4)])
    bullets = []

    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

    def spawn_bullet(self):
        bullet = Bullet(self.x + 200)
        self.controller.add_widget(bullet)
        self.controller.state["bullets"].append(bullet)

    def shoot(self):
        self.spawn_bullet()
        self.first, self.second = randint(0, 9), randint(0, 9)
        self.operation = f'{self.first} {self.operator} {self.second}'
        self.result = str(eval(self.operation))
        self.response = ''
        self.state = 'OFF'
        self.color = [1 for _ in range(4)]
