from kivy.uix.widget import Widget

from gun_administrator import GunAdministrator
from components.guns.gun import Gun


class WarZone(Widget):
    controller = None

    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        controller.add_widget(Gun(controller))
        controller.add_widget(GunAdministrator(controller))
        self.controller = controller

    def move_enemies(self):
        for enemy in self.controller.state["enemies"]:
            enemy.move()

    def kill_enemy(self, enemy):
        self.controller.remove_widget(enemy)
        self.controller.state["enemies"].remove(enemy)
        self.controller.state["killed_enemies"] += 1

    def kill_bullet(self, bullet):
        # This one only works with the simple gun.
        self.controller.state["bullets"].remove(bullet)
        self.controller.remove_widget(bullet)

    def update(self):
        self.move_enemies()
        for enemy in self.controller.state["enemies"]:
            for bullet in self.controller.state["bullets"]:
                if enemy.check_collision(bullet):
                    self.kill_bullet(bullet=bullet)
                    self.kill_enemy(enemy=enemy)
        for bullet in self.controller.state["bullets"]:
            bullet.move()
