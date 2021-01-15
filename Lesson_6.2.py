# задание 2
import asyncio
import time
import sys


class Road:

    def __init__(self, length, width, weight, cm):
        self._length = length
        self._width = width
        self._weight = weight
        self._cm = cm

    def tonnage(self):
        return self._length * self._width * self._weight * self._cm

my_array = Road(5000, 20, 25, 5)

print(my_array.tonnage()/1000)



