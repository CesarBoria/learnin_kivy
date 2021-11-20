from kivy.app import App

from mastering_imports.gun_administrator import Gun, GunAdministrator
from mastering_imports.war_zone import WarZone


class MyApp(App):
    def build(self):
        ob = WarZone()
        ob.add_widget(Gun(ob))
        ob.add_widget(GunAdministrator(ob))
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
