from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

from mastering_imports.objects import Sum, Sub, InputArea, Gun, GunChulo, Enemy


class WarZone(Widget):
    num_enemies = 10
    spawned_enemies = 0
    killed_enemies = 0
    enemies = []
    bullets = Gun.bullets
    bullets_Sum = GunChulo.bullets

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Clock.schedule_interval(self.update, 1 / 60)
        self.b = Clock.schedule_interval(self.spawn_enemy_simple, 2)
        Clock.schedule_interval(self.spawn_enemy_sum, 6)
        Clock.schedule_interval(self.spawn_enemy_sub, 7)

    def spawn_enemy_simple(self, dt):
        if self.num_enemies > self.spawned_enemies:
            enemy = Enemy(0)
            self.enemies.append(enemy)
            self.add_widget(enemy)
            self.spawned_enemies += 1

    def spawn_enemy_sum(self, dt):
        if self.num_enemies > self.spawned_enemies:
            enemy = Enemy(150)
            self.enemies.append(enemy)
            self.add_widget(enemy)
            self.spawned_enemies += 1

    def spawn_enemy_sub(self, dt):
        if self.num_enemies > self.spawned_enemies:
            enemy = Enemy(350)
            self.enemies.append(enemy)
            self.add_widget(enemy)
            self.spawned_enemies += 1

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.move()

    def kill_enemy(self, enemy):
        self.remove_widget(enemy)
        self.enemies.remove(enemy)
        self.killed_enemies += 1

    def kill_bullet(self, bullet):
        self.bullets.remove(bullet)  # This one only works with the simple gun.
        self.remove_widget(bullet)

    def game_over_routine(self):
        for enemy in self.enemies:
            if enemy.check_conquest():
                self.a.cancel()
                self.b.cancel()
                print('GAME OVER')

    def win_routine(self):
        if self.killed_enemies == self.num_enemies:
            self.a.cancel()
            self.b.cancel()
            print('WIN!')

    def update(self, dt):
        self.move_enemies()
        self.game_over_routine()
        self.win_routine()
        for enemy in self.enemies:
            for bullet in self.bullets:
                if enemy.check_collision(bullet):
                    self.kill_bullet(bullet=bullet)
                    self.kill_enemy(enemy=enemy)
            for bullet in self.bullets_Sum:
                if enemy.check_collision(bullet):
                    self.kill_bullet(bullet=bullet)
                    self.kill_enemy(enemy=enemy)
        for bullet in self.bullets:
            bullet.move('dt')

'''
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
            self.bullets.remove(bullet)  # This one only works with the simple gun.
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
'''