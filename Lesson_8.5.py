# задание 4-6

import math

class Storage():

 def __init__(self, area, volume, height, truck, security, video):
   self.area = area # площадь
   self.volume = volume # объем в единицах хранения
   self.height = height # высота потолка
   self.truck = truck # возможность принимать грузовой транспорт
   self.security = security # охрана объекта
   self.vide = video # наличие видеонаблюдения


 defaults = {'printer': 0, 'scanner': 0, 'xerox': 0, 'color': ''}

 @classmethod
 def my_input(cls, **kwargs): #метод обработки приема техники на склад
     Storage.defaults.update(kwargs)

 def __init__(self, *args, **kwargs):
     self.__dict__.update(Storage.defaults)

     keys = list(Storage.defaults.keys())
     for i, v in enumerate(args):
         if int(v) <= 0:
             raise print('Введите число единиц техники больше нуля ')
         self.__dict__[keys[i]] = v
     self.my_output(**kwargs)

 def my_output(self, **kwargs): #  метод списния техники со склада в отдел назначения
     self.__dict__.update(kwargs)

 def my_change(self, exit): #
     return (self.printer - exit.printer, self.scanner - exit.scanner, self.xerox - exit.xerox)

 def __repr__(self):
     return str(self.__dict__)


a = Storage(3,7,10) #,'белый') # число принтеров, сканнеров и ксероксов, поступивших на склад
print(a)

a.my_output(printer = 2, scanner = 3, xerox = 5)#, color = 'черный') # число принтеров, сканнеров и ксероксов, оставшихся на складе после списания
print(a)



class Ofeq:

 def __init__(self, speed, weight, height, color, format):
   self.speed = speed # скорость
   self.weight = weight # вес техники
   self.height = height # высота техники от пола
   self.color = color # цвет техники
   self.formst = format # формат работы техники


class Printer(Ofeq):

  def __init__(self, speed, weight, height, color, format):
        super().__init__(speed, weight, height, color, format)

        print(f'Поступили принтеры со скоростью распечатки {self.speed} лист/мин и {self.color} печатью')


class Scanner(Ofeq):
  def __init__(self, speed, weight, height, color, format):
        super().__init__(speed, weight, height, color, format)


class Xerox(Ofeq):
  def __init__(self, speed, weight, height, color, format):
        super().__init__(speed, weight, height, color, format)


b = Printer(60, 50, 100, 'цветной', 'full')






