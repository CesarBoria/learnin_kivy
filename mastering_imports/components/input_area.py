from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_string('''
<InputArea>:
    GridLayout:
        pos: 500, 0
        size: 200, 200
        rows: 2
        Button:
            text: '0'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '1'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '2'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '3'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '4'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '5'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '6'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '7'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '8'
            on_press: root.parent.type_number(self.text)
        Button:
            text: '9'
            on_press: root.parent.type_number(self.text)

''')


class InputArea(Widget):
    pass
