from kivy.uix.widget import Widget
from kivy.clock import Clock

from mastering_imports.objects import Gun, GunChulo, Enemy
from mastering_imports.result import Result


class WarZone(Widget):
    num_enemies = 10
    spawned_enemies = 0
    killed_enemies = 0
    enemies = []
    bullets = Gun.bullets
    bullets_Sum = GunChulo.bullets
    playing = True

    def __init__(self, info, **kwargs):
        super().__init__(**kwargs)
        self.info = info
        self.add_widget(self.info)
        self.update_event = Clock.schedule_interval(self.update, 1 / 60)
        self.spawn_enemy_event = Clock.schedule_interval(self.spawn_enemy_simple, 2)
        self.spawn_enemy_event_sum = Clock.schedule_interval(self.spawn_enemy_sum, 6)
        self.spawn_enemy_event_sub = Clock.schedule_interval(self.spawn_enemy_sub, 7)
        self.result = None
        self.speed = 0.1

    def spawn_enemy_simple(self, dt):
        if self.num_enemies > self.spawned_enemies:
            enemy = Enemy(0, self.speed)
            self.enemies.append(enemy)
            self.add_widget(enemy)
            self.spawned_enemies += 1

    def spawn_enemy_sum(self, dt):
        if self.num_enemies > self.spawned_enemies:
            enemy = Enemy(150, self.speed)
            self.enemies.append(enemy)
            self.add_widget(enemy)
            self.spawned_enemies += 1

    def spawn_enemy_sub(self, dt):
        if self.num_enemies > self.spawned_enemies:
            enemy = Enemy(350, self.speed)
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
        self.info.to_kill = str(self.num_enemies - self.killed_enemies)

    def kill_bullet(self, bullet):
        self.bullets.remove(bullet)
        self.remove_widget(bullet)

    def game_over_routine(self):
        for enemy in self.enemies:
            if enemy.check_conquest():
                self.playing = False
                percentage_killed = self.killed_enemies / self.num_enemies if self.killed_enemies != 0 else 0.05
                next_speed = percentage_killed * self.speed
                self.result = Result(self, 'L O S E R', next_speed)
                self.add_widget(self.result)
                self.speed = next_speed

    def win_routine(self):
        if self.killed_enemies == self.num_enemies:
            self.playing = False
            next_speed = self.speed + 0.1
            self.result = Result(self, 'W I N N E R', next_speed)
            self.add_widget(self.result)
            self.speed = next_speed

    def clean_screen(self):
        for enemy in self.enemies:
            self.remove_widget(enemy)
        for bullet in self.bullets:
            self.remove_widget(bullet)
        self.remove_widget(self.result)

    def restart(self):
        self.num_enemies = 10
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.playing = True
        self.update_event = Clock.schedule_interval(self.update, 1 / 60)
        self.spawn_enemy_event = Clock.schedule_interval(self.spawn_enemy_simple, 2)
        self.spawn_enemy_event_sum = Clock.schedule_interval(self.spawn_enemy_sum, 6)
        self.spawn_enemy_event_sub = Clock.schedule_interval(self.spawn_enemy_sub, 7)
        self.clean_screen()
        self.enemies = []
        print(self.speed)

    def cancel_events(self):
        self.spawn_enemy_event.cancel()
        self.spawn_enemy_event_sub.cancel()
        self.spawn_enemy_event_sum.cancel()
        self.update_event.cancel()

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
        if not self.playing:
            self.cancel_events()
