from functools import partial

from kivy.app import App
from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

from mastering_imports.war_zone import WarZone

Builder.load_string('''
<Info>:
    pos: 500, 200
    GridLayout:
        pos: root.pos
        size: 200, 100
        cols: 2
        Label:
            text: 'Zoombees to kill:'
        Label:
            text: root.to_kill
        Label:
            text: 'Zoombees killed:'
        Label:
            text: root.killed
    
''')


class Info(Widget):
    killed = StringProperty()
    to_kill = StringProperty()

    def __init__(self, WZ, **kwargs):
        super().__init__(**kwargs)
        self.WZ = WZ
        self.killed = str(WZ.killed_enemies)
        self.to_kill = str(WZ.num_enemies - WZ.killed_enemies)
        Clock.schedule_interval(partial(self.a), 1)

    @property
    def get_killed(self):
        self.killed = self.WZ.killed_enemies
        return self.killed

    def a(self, dt):
        self.killed = str(self.WZ.killed_enemies)
        self.to_kill = str(self.WZ.num_enemies - self.WZ.killed_enemies)

'''
class MyApp(App):
    def build(self):
        ob = Info()
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
'''