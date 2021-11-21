from functools import partial

from kivy.app import App
from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

from war_zone import WarZone

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

    def __init__(self, state, **kwargs):
        super().__init__(**kwargs)
        self.state = state
        self.killed = str(state["killed_enemies"])
        self.to_kill = str(state["num_enemies"] - state["killed_enemies"])

    def update(self):
        self.killed = str(self.state["killed_enemies"])
        self.to_kill = str(
            self.state["num_enemies"] - self.state["killed_enemies"])
