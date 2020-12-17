# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# задание 1
name = input("Как Вас зовут? ")

age = int(input("Сколько Вам лет? "))

year = int(input("Какой сейчас год? "))

desease = str.lower(input("Вы болели коронавирусом? "))

if desease == "да":
    print("Вас зовут",name,"Вам", age)
    print("Вы переболели covid_19")
else:
    print("Вас зовут ", name, ", Вам ", age)
    print("Вам повезло, Вы не болели covid_19")

# задание 2

time = int(input("Введите время в секундах "))

hour = time // 3600

min = (time % 3600) // 60

sec = time - (hour * 3600) - (min * 60)

print(f"{hour}:{min}:{sec}")

# задание 3

n = int(input("Введите число от 0 до 9 "))

a = int(n)

b = int(str(n) + str(n))

c = int(str(n) + str(n) + str(n))

print(a + b + c)

# задание 4

n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n > 0:
    n = n // 10
    if n % 10 > max:
        max = n % 10
        continue
else:
     print("Максимальная цифра в числе ", max)

# задание 5

revenue = int(input("Введите объем выручки предприятия "))
costs = int(input("Введите объем издержек фирмы "))

if revenue > costs:
    print("Бизнес прибыльный. Рентабельность составляет ",((revenue - costs)/revenue)*100,"%")
    staff = int(input("Какова численность сотрудников фирмы? "))
    print("Прибыль на одного сотрудника составляет ",(revenue - costs)/staff,"руб.")
else:
    print("Бизнес убыточный")

# задание 6

a = int(input("Результат первого дня пробежек, км "))
b = int(input("Целевой результат пробежек, км "))

i = 0

while a < b:
    a = a * 1.1
    i += 1
    continue
else:
    print("Спортсмен достигнет результата на ",i,"день")



