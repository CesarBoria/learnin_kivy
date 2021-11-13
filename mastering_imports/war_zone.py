from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

from mastering_imports.objects import Sum, Sub, InputArea, Gun, GunChulo, Enemy


class WarZone(Widget):
    enemies = []
    bullets = Gun.bullets
    bullets_Sum = GunChulo.bullets
    # bullets_Sub = GunChulo.bullets

    def spawn_enemy(self, dt):
        enemy = Enemy()
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
        self.bullets_Sum.clear()
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


if __name__ == '__main__':
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


    class MyApp(App):
        def build(self):
            ob = WarZone()
            ob.add_widget(Gun())
            ob.add_widget(GunAdministrator())
            Clock.schedule_interval(ob.update, 1 / 60)
            Clock.schedule_interval(ob.spawn_enemy, 2)
            return ob


    app_instance = MyApp()
    app_instance.run()
