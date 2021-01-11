# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# задание 1

rand_list = ('привет',('п','р','и','в','е','т'),{777, 1},(bool()), 2, {"A": 1,"b": 14}, 3.3,['т', 'и', 'п'],None)

for el in rand_list:
    print(type(el))

# задание 2

count = int(input("Введите число элементов списка " ))

list2 = []

i = 0

el = 0

while i < count:
    list2.append(input("Введите значение списка "))
    i += 1
for var in range(int(len(list2)/2)):
     list2[el], list2[el + 1] = list2[el + 1], list2[el]
     el += 2
print(list2)

# задание 3

list = ['весна', 'лето', 'осень', 'зима']

dict = {1 : 'весна', 2 : 'лето', 3 : 'осень', 4 : 'зима'}

month = int(input("Введите номер месяца "))

if month == 3 or month == 4 or month == 5:
    #print(dict.get(1))
    print(list[0])
elif month == 6 or month == 7 or month == 8:
    #print(dict.get(2))
    print(list[1])
elif month == 9 or month == 10 or month == 11:
    #print(dict.get(3))
    print(list[2])
elif month == 12 or month == 1 or month == 2:
    #print(dict.get(4))
    print(list[3])
else:
    print("Введите другой месяц")

# задание 4


words = input("Введите несколько слов через пробелы ")

a = ''

i = 0

for el in range(words.count(' ') + 1):
    a = words.split()
    if len(str(a)) <= 10:
        print(f" {i} {a [el]}")
        i += 1
    else:
        print(f" {i} {a [el] [0:10]}")
        i += 1



# задание 5

list = [7, 5, 3, 3, 2]

var = int(input("Введите натуральное число "))


while var != 5:
 for el in range(len(list)):
    if list[el] == var:
        list.insert(el + 1, var)
        break
    elif list[0] < var:
        list.insert(0, var)
    elif list[-1] > var:
        list.append(var)
    elif list[el] > var and list[el + 1] < var:
        list.insert(el +1, var)
    print(f"Список {list}")
    var = int(input("Введите натуральное число "))


# задание 6

prod = []

while input("Добавить товар (да/нет) ") == 'да':
    numb = int(input('Присвойте номер товару от 1 до 3 '))
    char = {}
    while input("Добавить характеристики товара (да/нет) ") == 'да':
        char_key = input("Введите название товара ")
        char_val = input("Введите стоимость товара ")
        char[char_key] = char_val
    prod.append(tuple([numb, char]))
    print(prod)

ana = {}
for pr in prod:
    for char_key, char_val in pr[1].items():
        if char_key in ana:
            ana[char_key].append(char_val)
        else:
            ana[char_key] = [char_val]
print(ana)