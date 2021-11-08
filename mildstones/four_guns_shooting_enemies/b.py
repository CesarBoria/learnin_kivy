from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, StringProperty
from kivy.clock import Clock
from random import random, randint

Builder.load_string('''
<InputArea>:
    rows: 2
    Button:
        text: '0'
        on_press: root.type_number(self.text)
    Button:
        text: '1'
        on_press: root.type_number(self.text)
    Button:
        text: '2'
        on_press: root.type_number(self.text)
    Button:
        text: '3'
        on_press: root.type_number(self.text)
    Button:
        text: '4'
        on_press: root.type_number(self.text)
    Button:
        text: '5'
        on_press: root.type_number(self.text)
    Button:
        text: '6'
        on_press: root.type_number(self.text)
    Button:
        text: '7'
        on_press: root.type_number(self.text)
    Button:
        text: '8'
        on_press: root.type_number(self.text)
    Button:
        text: '9'
        on_press: root.type_number(self.text)
<Gun>:
    Button:
        text: root.operation + '\\n' + root.response
        font_size: 50
        on_release: root.parent.button_clicked(root)
        background_color: root.color
<MainWidget>:
    rows: 2
    GunArea:        
    InputArea:
''')


class Gun(RelativeLayout):
    first, second = randint(0, 9), randint(0, 9)
    operator = '+'
    operation = f'{first} {operator} {second}'
    operation_kv = StringProperty(operation)
    result = str(eval(operation))
    response = StringProperty('')
    state = 'OFF'
    color = ListProperty([1 for i in range(4)])

    def shoot(self):
        print('PIUM')
        self.first, self.second = randint(0, 9), randint(0, 9)
        self.operation = f'{self.first} {self.operator} {self.second}'
        self.result = str(eval(self.operation))
        self.response = ''
        GunArea.update_colors(GunArea)


class Sum(Gun):
    first, second = randint(0, 9), randint(0, 9)
    operator = '+'
    operation = f'{first} {operator} {second}'
    result = str(eval(operation))


class Sub(Gun):
    limit = randint(0, 9)
    first, second = randint(limit, 9), randint(0, limit)
    operator = '-'
    operation = f'{first} {operator} {second}'
    result = str(eval(operation))


class GunArea(BoxLayout):
    guns = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        gun1 = Sum()
        gun2 = Sub()
        self.add_widget(gun1)
        self.add_widget(gun2)
        self.guns.append(gun1)
        self.guns.append(gun2)

    def all_off(self):
        for gun in self.guns:
            gun.state = 'OFF'
            if gun.result != gun.response:
                gun.response = ''

    def button_clicked(self, gun):
        self.all_off()
        gun.state = 'ON'
        self.update_colors()
        if gun.color == [0, 1, 0, 1]:
            gun.shoot()

    def update_colors(self):
        for gun in self.guns:
            if gun.response == gun.result:
                gun.color = [0, 1, 0, 1]
            elif gun.state == 'ON' and gun.response != '':
                gun.color = [1, 0, 0, 1]
            elif gun.state == 'ON' and gun.response == '':
                gun.color = [0, 0, 1, 1]
            else:
                gun.color = [1, 1, 1, 1]


class InputArea(GridLayout):
    @staticmethod
    def type_number(text):
        for gun in GunArea.guns:
            if gun.state == 'ON':
                gun.response += text
                print(gun.result, gun.response)
        GunArea.update_colors(GunArea)


class MainWidget(GridLayout):
    pass


class MyApp(App):
    def build(self):
        ob = MainWidget()
        return ob


if __name__ == '__main__':
    app_instance = MyApp()
    app_instance.run()
