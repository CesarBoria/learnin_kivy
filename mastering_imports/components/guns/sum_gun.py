from random import randint
from components.guns.gun_operation import GunChulo


class Sum(GunChulo):
    first, second = randint(0, 9), randint(0, 9)
    operator = '+'
    operation = f'{first} {operator} {second}'
    result = str(eval(operation))
