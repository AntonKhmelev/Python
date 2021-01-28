# задание 1
import time

class Date:

 def __init__(self, day, month, year):
     self.day = day
     self.month =  month
     self.year = year

 def __str__(self):
     return f'Дата: {self.day}-{self.month}-{self.year}'

 @classmethod
 def str_into_date(cls, day, month, year):
     dt = time.strptime(f'{day}{month}{year}','%d%m%Y')
     return print(time.strftime('%d-%m-%Y', dt))

 @staticmethod
 def validation(day, month, year):
     if day not in range(1, 32):
         print("День не прошел проверку")
     elif month not in range(1, 13):
         print("Месяц не прощел проверку")
     elif year not in range(2000, 2022):
         print("Год не прошел проверку")
     else:
         print("Проверка даты успешно пройдена!")


my_date = Date(21, 12, 2020)

j = Date.str_into_date(21,12,2020)

print(my_date)

print(j)

print(Date.validation(21, 12, 2020))


