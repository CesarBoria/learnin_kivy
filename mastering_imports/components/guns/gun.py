from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

from components.bullet import Bullet

Builder.load_string('''
<Gun>:
    Button:
        text: 'GUN'
        on_press: root.shoot()
''')


class Gun(Widget):

    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

    def spawn_bullet(self):
        bullet = Bullet(x=self.x + 45)
        self.controller.add_widget(bullet)
        self.controller.state["bullets"].append(bullet)

    def shoot(self):
        self.spawn_bullet()
