from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget

#from mildstones.four_guns_shooting_enemies.c import Gun, GunAdministrator, Enemy, GunChulo


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
        #bullet.shooting_event.unschedule() The Gun has the property shooting event, not the bullet.
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
        ob.add_widget(Gun())
        ob.add_widget(GunAdministrator())
        Clock.schedule_interval(ob.update, 1 / 60)
        Clock.schedule_interval(ob.spawn_enemy, 2)
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
