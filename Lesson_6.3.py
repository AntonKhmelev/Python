# задание 3
import asyncio
import time
import sys


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage,'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
           super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name +' '+ self.surname + ' ' + self.position

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

my_worker = Position('Алексей', 'Австральный', 'борт-механик', 15000, 10000)

print(my_worker.get_full_name(), my_worker.get_total_income())



