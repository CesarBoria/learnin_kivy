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
        # Label:
        #     text: 'Zoombees killed:'
        # Label:
        #     text: root.killed
    
''')


class Info(Widget):
    # killed = StringProperty()
    to_kill = StringProperty('10')

'''
class MyApp(App):
    def build(self):
        ob = Info()
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
'''