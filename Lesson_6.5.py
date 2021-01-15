# задание 5
import asyncio
import time
import sys


class Stationery:

    def __init__(self, title):
        self.title = title


    def draw(self):
        return f'Запус отрисовки {self.title}'

class Pen(Stationery):

    def draw(self):
        return f'Отрисовка синей щариковой {self.title} начинается'

class Pencil(Stationery):

    def draw(self):
        return f'Набросаем эскиз на бумагу {self.title}'

class Handle(Stationery):

    def draw(self):
        return f'Обведем {self.title} ключевые темы урока'

my_pen = Pen('ручкой')

my_pencil = Pencil('карандашом')

my_handle = Handle('маркером')

print(my_pen.draw())
print(my_pencil.draw())
print(my_handle.draw())






