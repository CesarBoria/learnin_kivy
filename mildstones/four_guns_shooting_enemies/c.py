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


class String:
    pass


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
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
<Bullet>:
    canvas.after:
        Color:
            rgba: 1, 0, 0, 0.5
        Rectangle:
            pos: self.pos
            size: self.size
    canvas:
        Rectangle:
            pos: self.width/2-5, self.y
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

    def move(self):
        self.x = 00
        self.y = self.parent.height - 100 - self.walked
        self.walked += 1

    def check_collision(self, bullet):
        if self.collide_widget(bullet):
            return True

    def check_conquest(self):
        if self.y < 0:
            return True


class Bullet(Widget):
    @staticmethod
    def appear():
        t = Bullet()

    def move(self, dt):
        self.y += 10


class Gun(Widget):
    bullets = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.b = None
        self.shooting_event = None

    def spawn_bullet(self):
        self.b = Bullet()
        self.b.appear()
        self.add_widget(self.b)
        self.bullets.append(self.b)

    def shoot(self):
        self.spawn_bullet()
        self.shooting_event = Clock.schedule_interval(self.b.move, 1 / 60)


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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.b = None
        self.shooting_event = None

    def spawn_bullet(self):
        self.b = Bullet()
        self.b.appear()
        self.add_widget(self.b)
        self.bullets.append(self.b)

    def shoot(self):
        self.spawn_bullet()
        self.shooting_event = Clock.schedule_interval(self.b.move, 1 / 60)

        print('PIUM')
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


class InputArea(Widget):
    pass


class GunAdministrator(Widget):
    guns = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        gun1 = Sum()
        gun2 = Sub()
        gun2.pos = 200, 0
        gun2.size = 200, 200
        gun1.pos = 0, 0
        gun1.size = 200, 200
        self.add_widget(gun1)
        self.add_widget(gun2)
        self.guns.append(gun1)
        self.guns.append(gun2)
        self.add_widget(InputArea())

    def all_off(self):
        for gun in self.guns:
            gun.state = 'OFF'
            if gun.result != gun.response:
                gun.response = ''

    def button_clicked(self, gun):
        self.all_off()
        gun.state = 'ON'
        self.update_colors()
        if gun.color == [0, 1, 0, 1]:
            gun.shoot()

    def update_colors(self):
        for gun in self.guns:
            if gun.response == gun.result:
                gun.color = [0, 1, 0, 1]
            elif gun.state == 'ON' and gun.response != '':
                gun.color = [1, 0, 0, 1]
            elif gun.state == 'ON' and gun.response == '':
                gun.color = [0, 0, 1, 1]
            else:
                gun.color = [1, 1, 1, 1]

    def type_number(self, text):
        print(text)
        for gun in self.guns:
            if gun.state == 'ON':
                gun.response += text
        self.update_colors()


class WarZone(Widget):
    enemies = []
    bullets = Gun.bullets
    bullets_Sum = GunChulo.bullets

    def spawn_enemy(self, dt):
        enemy = Enemy()
        self.enemies.append(enemy)
        self.add_widget(enemy)

    def update(self, dt):
        for enemy in self.enemies:
            enemy.move()
            for bullet in self.bullets:
                if enemy.check_collision(bullet):
                    self.bullets.clear()
                    self.remove_widget(bullet)
                    self.enemies.remove(enemy)
                    self.remove_widget(enemy)
            for bullet in self.bullets_Sum:
                if enemy.check_collision(bullet):
                    self.bullets.clear()
                    self.remove_widget(bullet)
                    self.enemies.remove(enemy)
                    self.remove_widget(enemy)
            if enemy.check_conquest():
                pass  # TODO: Run Game Over Routine.
        for bullet in self.bullets:
            bullet.move('dt')


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
