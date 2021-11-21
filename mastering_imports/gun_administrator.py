from kivy.uix.widget import Widget

from components.input_area import InputArea
from components.guns.sum_gun import Sum
from components.guns.sub_gun import Sub


class GunAdministrator(Widget):
    guns = []

    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        gun1 = Sum(controller)
        gun2 = Sub(controller)
        gun2.pos = 200, 0
        gun2.size = 200, 200
        gun1.pos = 0, 0
        gun1.size = 200, 200
        self.add_widget(gun1)
        self.add_widget(gun2)
        self.guns.append(gun1)
        self.guns.append(gun2)
        self.add_widget(InputArea())

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

    def type_number(self, text):
        print(text)
        for gun in self.guns:
            if gun.state == 'ON':
                gun.response += text
        self.update_colors()
