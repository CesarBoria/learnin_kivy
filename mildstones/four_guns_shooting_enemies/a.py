from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import NumericProperty, ObjectProperty, ListProperty
from kivy.clock import Clock

Builder.load_string('''
<Enemy>:
    size: root.s, root.s
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
<Bullet>:
    canvas:
        Rectangle:
            pos: self.width/2-5, self.y
            size: 10, 100
<Gun>:
    Button:
        text: 'GUN'
        on_press: root.shoot()
''')


class Enemy(Widget):
    s = NumericProperty(100)
    walked = 0

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


class NonThings(Widget):
    enemies = []
    bullets = Gun.bullets

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
            if enemy.check_conquest():
                print('Lost')
        for bullet in self.bullets:
            bullet.move('dt')
        print(self.bullets)


class MyApp(App):
    def build(self):
        ob = NonThings()
        g = Gun()
        ob.add_widget(g)
        Clock.schedule_interval(ob.update, 1 / 60)
        Clock.schedule_interval(ob.spawn_enemy, 2)
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
