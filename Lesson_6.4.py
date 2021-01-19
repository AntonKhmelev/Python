# задание 4
import asyncio
import time
import sys


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_to_left(self):
        return f'{self.name} повернула влево'

    def turn_to_right(self):
        return f'{self.name} повернула вправо'

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
           super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость машиной {self.name} превышена!')
        else:
            print(f'Скорость машиной {self.name} соблюдается!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
           super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость машиной {self.name} превышена!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
           super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print(f'Машина {self.name} полицейская!')
        else:
            pass



volga = PoliceCar(100,'Синий','Волга 2410', True)

zhiguli = SportCar(120,'Вишневая','Девятка', False)

porsh = WorkCar(200, 'Желтый', '911', False)

oka = TownCar(50, 'Зеленый', 'Ока', False)


print(volga.police())
print(volga.show_speed())

print(porsh.show_speed())
print(oka.show_speed())





