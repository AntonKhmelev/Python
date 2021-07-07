# задание 1
import time
import datetime


class Date:
 def __init__(self, obj):
     self.obj = obj

     print(type(self.obj))
     print(self.obj)

 @classmethod
 def str_into_date(cls, obj):

     dt = time.strptime(f'{obj}','%d-%m-%Y')
     return print(time.strftime('%d %B %Y', dt))

 @staticmethod
 def validation(obj):
   c = []
   for i in obj.split('-'):
     c.append(i)
     print(c)

   if int(c[0]) not in range(1, 32):
        print("День не прошел проверку!")
   elif int(c[1]) not in range(1, 13):
        print("Месяц не прощел проверку!")
   elif int(c[2]) not in range(2000, 2022):
        print("Год не прошел проверку!")
   else:
        print("Проверка даты успешно пройдена!")

b = input('Введите дату в формате "день-месяц-год" ')
a = Date(b)
a = Date.str_into_date(b)
c = Date.validation(input('Повторно введите дату в том же формате для валидации '))

