# задание 1
import numpy as np

class Cells:
      def __init__(self, subcells):
          self.subcells = subcells

      def __add__(self, other):
            print(f'Результат сложения {(int(self.subcells) + int(other.subcells))}')
            return

      def __sub__(self, other):
          if (int(self.subcells) - int(other.subcells)) > 0:
            print(f"Разность ячеек клеток составляет {(int(self.subcells) - int(other.subcells))}")
          else:
            print(f"Разность ячеек клеток отрицательная")
            return

      def __mul__(self, other):
            print(f'Результат умножения {(int(self.subcells) * int(other.subcells))}')
            return

      def __floordiv__(self, other):
            print(f'Результат деления клеток {(int(self.subcells) // int(other.subcells))}')
            return

      def make_order(self, cells):
          row = ''
          for i in range(int(self.subcells / cells)):
              row += f'{"*" * cells} \\ n'
          row += f'{"*" * (self.subcells % cells)}'
          return row


my_cells1 = Cells(10)
my_cells2 = Cells(11)


print(my_cells1 + my_cells2)

print(my_cells1 - my_cells2)

print(my_cells1 * my_cells2)

print(my_cells1 // my_cells2)

print(my_cells1.make_order(6))

print(my_cells1.make_order(10))


# декоратор @property затруднился построить, не совсем понял, как это здесь реализуется - то ли мы к size делаем декоратор и приклеиваем @property ко второй функции height,
# то ли для обеих функций size и height строится некая третья декорирующая функция


