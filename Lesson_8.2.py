# задание 2

class ZeroDiv:

 def __init__(self, dible, disor):
     self.dible = dible
     self.disor = disor

     try:
        res = self.dible/self.disor
     except ZeroDivisionError:
        print("Внимание, делить на ноль нельзя!")
     else:
        print(f"Деление произведено корректно. Частное равно {round(res)}")
     return

a = int(input('Введите делимое '))
b = int(input('Введите делитель '))

c = ZeroDiv(a,b)






