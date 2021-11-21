from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from functools import partial
from war_zone import WarZone
from info_display import Info
from components.enemy import Enemy
from constants import ENEMY_SPAWN_X


class GameScreen(Widget):
    state = {
        "num_enemies": 10,
        "spawned_enemies": 0,
        "killed_enemies": 0,
        "enemies": [],
        "bullets": [],
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game_interval = Clock.schedule_interval(self.update, 1 / 60)
        self.enemy_spawn_simple_interval = Clock.schedule_interval(
            partial(Enemy.spawn, self, ENEMY_SPAWN_X["SIMPLE"]), 2)
        self.enemy_spawn_sum_interval = Clock.schedule_interval(
            partial(Enemy.spawn, self, ENEMY_SPAWN_X["SUM"]), 6)
        self.enemy_spawn_sub_interval = Clock.schedule_interval(
            partial(Enemy.spawn, self, ENEMY_SPAWN_X["SUB"]), 7)
        self.warzone = WarZone(self)
        self.info = Info(self.state)
        self.add_widget(self.warzone)
        self.add_widget(self.info)

    def game_over_routine(self):
        for enemy in self.state["enemies"]:
            if enemy.check_conquest():
                self.end_game('GAME OVER')

    def win_routine(self):
        if self.state["killed_enemies"] == self.state["num_enemies"]:
            self.end_game('WIN!')

    def end_game(self, text):
        self.game_interval.cancel()
        self.enemy_spawn_simple_interval.cancel()
        self.enemy_spawn_sum_interval.cancel()
        self.enemy_spawn_sub_interval.cancel()
        print(text)

    def update(self, dt):
        self.warzone.update()
        self.info.update()
        self.game_over_routine()
        self.win_routine()
