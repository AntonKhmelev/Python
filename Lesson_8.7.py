# задание 7
import numpy as np

class Complex:
      def __init__(self, arg1):
          self.arg1 = arg1


      def __add__(self, other):
           return f'Результат сложения {(int(self.arg1) + int(other.arg1))}'


      def __mul__(self, other):
           return f'Результат умножения {(int(self.arg1) * int(other.arg1))}'


my_arg1 = Complex(-1)
my_arg2 = Complex(-1)


print(my_arg1 + my_arg2)

print(my_arg1 * my_arg2)




