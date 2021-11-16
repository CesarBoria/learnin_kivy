from kivy.app import App
from kivy.clock import Clock

from mastering_imports.gun_administrator import Gun, GunAdministrator
from mastering_imports.war_zone import WarZone


class MyApp(App):
    def build(self):
        ob = WarZone()
        ob.add_widget(Gun(ob))
        ob.add_widget(GunAdministrator(ob))
        Clock.schedule_interval(ob.update, 1 / 60)
        Clock.schedule_interval(ob.spawn_enemy, 2)
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
