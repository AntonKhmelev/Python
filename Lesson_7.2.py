# задание 1
import numpy as np

class Clothes:
      def __init__(self, coat, suit):
          self.coat = coat
          self.suit = suit


      #def decorator(self):
      def size(self):
              print(f"Расход материала на пальто составляет {int(self.coat/6.5 + 0.5)}")
              return

      #@property
      def height(self):
              print(f"Расход материала на костюм составляет {int(self.suit*2 + 0.3)}")
              #return

              print(f'ОБщий расход материала составляет {int(self.suit*2 + 0.3) + int(self.coat/6.5 + 0.5)}')
              return

my_clothes = Clothes(10,4)

my_clothes.size()
my_clothes.height()

# декоратор @property затруднился построить, не совсем понял, как это здесь реализуется - то ли мы к size делаем декоратор и приклеиваем @property ко второй функции height,
# то ли для обеих функций size и height строится некая третья декорирующая функция


