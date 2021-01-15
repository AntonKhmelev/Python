# задание 1
import asyncio
import time
import sys


class TrafficLight:

    def __init__(self, color):
        self.color = color

    def running(self):
        print(f'цвет {self.color}')

r = TrafficLight('КРАСНЫЙ')
y = TrafficLight('ЖЕЛТЫЙ')
g = TrafficLight('ЗЕЛЕНЫЙ')


r.running()
time.sleep(7)


y.running()
time.sleep(2)

g.running()
time.sleep(5)


# не смог сообразить, как сделать затирку сообщений по прошествии отведенного времени, чтобы появлялось только одно сообщение всякий раз

