from kivy.app import App
from kivy.clock import Clock

from mastering_imports.areas import WarZone, Gun, GunAdministrator


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
