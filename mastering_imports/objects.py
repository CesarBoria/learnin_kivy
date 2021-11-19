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

    def __init__(self, x, **kwargs):
        super().__init__(**kwargs)
        self.x = x

    def move(self):
        self.y = self.parent.height - 100 - self.walked
        self.walked += 1

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
        self.b = Bullet(x=self.x+45)
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
        self.b = Bullet(self.x+200)
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


class InputArea(Widget):
    pass


if __name__ == '__main__':
    class GunAdministrator(Widget):
        guns = []

        def __init__(self, GUI, **kwargs):
            super().__init__(**kwargs)
            self.GUI = GUI
            gun1 = Sum(self.GUI)
            gun2 = Sub(self.GUI)
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

        # bullets_Sub = GunChulo.bullets

        def spawn_enemy_simple(self, dt):
            enemy = Enemy(0)
            self.enemies.append(enemy)
            self.add_widget(enemy)

        def spawn_enemy_sum(self, dt):
            enemy = Enemy(150)
            self.enemies.append(enemy)
            self.add_widget(enemy)

        def spawn_enemy_sub(self, dt):
            enemy = Enemy(350)
            self.enemies.append(enemy)
            self.add_widget(enemy)

        def move_enemies(self):
            for enemy in self.enemies:
                enemy.move()

        def kill_enemy(self, enemy):
            self.remove_widget(enemy)
            self.enemies.remove(enemy)

        def kill_bullet(self, bullet):
            # self.bullets.remove(bullet)  # This one only works with the simple gun.
            # bullet.shooting_event.unschedule() The Gun has the property shooting event, not the bullet.
            self.bullets.clear()
            self.remove_widget(bullet)

        def update(self, dt):
            self.move_enemies()
            for enemy in self.enemies:
                for bullet in self.bullets:
                    if enemy.check_collision(bullet):
                        self.kill_bullet(bullet=bullet)
                        self.kill_enemy(enemy=enemy)
                for bullet in self.bullets_Sum:
                    if enemy.check_collision(bullet):
                        self.kill_bullet(bullet=bullet)
                        self.kill_enemy(enemy=enemy)
                if enemy.check_conquest():
                    pass  # TODO: Run Game Over Routine.
            for bullet in self.bullets:
                bullet.move('dt')


    class MyApp(App):
        def build(self):
            ob = WarZone()
            ob.add_widget(Gun(ob))
            ob.add_widget(GunAdministrator(ob))
            Clock.schedule_interval(ob.update, 1 / 60)
            Clock.schedule_interval(ob.spawn_enemy_simple, 2)
            Clock.schedule_interval(ob.spawn_enemy_sum, 6)
            Clock.schedule_interval(ob.spawn_enemy_sub, 7)
            return ob


    app_instance = MyApp()
    app_instance.run()
