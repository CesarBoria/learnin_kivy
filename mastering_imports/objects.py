from random import randint

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty
from kivy.clock import Clock

Builder.load_string('''
<InputArea>:
    GridLayout:
        pos: 500, 0
        size: 200, 200
        rows: 2
        Button:
            text: '0'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '1'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '2'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '3'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '4'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '5'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '6'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '7'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '8'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '9'
            on_press: root.parent.type_number(self.text)

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
<Bullet>:
    canvas.after:
        Color:
            rgba: 1, 0, 0, 0.5
        Rectangle:
            pos: root.pos
            size: root.size
            size: 10, 100
<GunChulo>:
    Button:
        text: root.operation + '\\n' + root.response
        font_size: 50
        on_release: root.parent.button_clicked(root)
        background_color: root.color
        pos: 100, 0
<Gun>:
    Button:
        text: 'GUN'
        on_press: root.shoot()
''')


class Enemy(Widget):
    s = NumericProperty(100)
    walked = 0

    def __init__(self, x, speed, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.speed = speed

    def move(self):
        self.y = self.parent.height - 100 - self.walked
        self.walked += self.speed

    def check_collision(self, bullet):
        if self.collide_widget(bullet):
            return True

    def check_conquest(self):
        if self.y < 0:
            return True


class Bullet(Widget):
    def __init__(self, x, **kwargs):
        super().__init__(**kwargs)
        self.x = x

    def move(self, dt):
        self.y += 10


class Gun(Widget):
    bullets = []

    def __init__(self, GUI, **kwargs):
        super().__init__(**kwargs)
        self.GUI = GUI
        self.b = None
        self.shooting_event = None

    def spawn_bullet(self):
        self.b = Bullet(x=self.x + 45)
        self.GUI.add_widget(self.b)
        self.GUI.bullets.append(self.b)

    def shoot(self):
        self.spawn_bullet()


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

    def __init__(self, holder, **kwargs):
        super().__init__(**kwargs)
        self.holder = holder
        self.b = None
        self.shooting_event = None

    def spawn_bullet(self):
        self.b = Bullet(self.x + 200)
        self.holder.add_widget(self.b)
        self.holder.bullets.append(self.b)

    def shoot(self):
        self.spawn_bullet()
        self.first, self.second = randint(0, 9), randint(0, 9)
        self.operation = f'{self.first} {self.operator} {self.second}'
        self.result = str(eval(self.operation))
        self.response = ''
        self.state = 'OFF'
        self.color = [1 for _ in range(4)]


class Sum(GunChulo):
    first, second = randint(0, 9), randint(0, 9)
    operator = '+'
    operation = f'{first} {operator} {second}'
    result = str(eval(operation))


class Sub(GunChulo):
    limit = randint(0, 9)
    first, second = randint(limit, 9), randint(0, limit)
    operator = '-'
    operation = f'{first} {operator} {second}'
    result = str(eval(operation))

    def shoot(self):  # We override the method so that the limit applies at every shoot.
        self.spawn_bullet()
        limit = randint(0, 9)
        self.first, self.second = randint(limit, 9), randint(0, limit)
        self.operation = f'{self.first} {self.operator} {self.second}'
        self.result = str(eval(self.operation))
        self.response = ''
        self.state = 'OFF'
        self.color = [1 for _ in range(4)]


class InputArea(Widget):
    pass
