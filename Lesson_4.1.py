
# задача 1
import sys
print(sys.argv)

arguments = sys.argv[1:]

norm = int(arguments[0])
print('Выработка в часах ', norm)
rate = int(arguments[1])
print('Почасовая ставка ', rate)
prem = int(arguments[2])
print('Размер премии ', prem)

salary = (norm * rate) + prem

print('Размер заработной платы составляет', salary, 'руб.')



