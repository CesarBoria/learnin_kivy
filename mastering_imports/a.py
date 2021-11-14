from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
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
    def move(self, dt):
        self.y += 10


class Gun(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.b = None
        self.shooting_event = None
        self.GUI = MainGUI()

    def spawn_bullet(self):
        self.b = Bullet()
        main_gui.add_widget(self.b)
        main_gui.bullets.append(self.b)

    def shoot(self):
        self.spawn_bullet()
        self.shooting_event = Clock.schedule_interval(self.b.move, 1 / 60)


class MainGUI(Widget):
    enemies = []
    bullets = []

    def spawn_enemy(self, dt):
        enemy = Enemy()
        self.enemies.append(enemy)
        self.add_widget(enemy)

    def update(self, dt):
        for enemy in self.enemies:
            enemy.move()
            for bullet in self.bullets:
                if enemy.check_collision(bullet):
                    self.remove_widget(enemy)  # Remove the enemy from the screen.
                    self.enemies.remove(enemy)  # Remove the colliding enemy from the list of enemies.

                    self.remove_widget(bullet)  # Remove the bullet from the screen.
                    self.bullets.remove(bullet)  # Remove the bullet from the list of bullets.


main_gui = MainGUI()
main_gui.add_widget(Gun())


class MyApp(App):
    def build(self):
        # ob = WarZone()
        # ob.add_widget(Gun())
        Clock.schedule_interval(main_gui.update, 1 / 60)
        Clock.schedule_interval(main_gui.spawn_enemy, 2)
        return main_gui


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
