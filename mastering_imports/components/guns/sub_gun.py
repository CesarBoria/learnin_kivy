from random import randint
from components.guns.gun_operation import GunChulo


class Sub(GunChulo):
    limit = randint(0, 9)
    first, second = randint(limit, 9), randint(0, limit)
    operator = '-'
    operation = f'{first} {operator} {second}'
    result = str(eval(operation))

    def shoot(self):
        limit = randint(0, 9)
        self.first, self.second = randint(limit, 9), randint(0, limit)
        super().shoot()
