from kivy.app import App
from kivy.clock import Clock

from mastering_imports.gun_administrator import Gun, GunAdministrator
from mastering_imports.info_display import Info
from mastering_imports.war_zone import WarZone


class MyApp(App):
    def build(self):
        ob = WarZone()
        ob.add_widget(Gun(ob))
        ob.add_widget(GunAdministrator(ob))
        ob.add_widget(Info(ob))
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
