# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# задание 3

def my_func():
    global args
    var1 = input("Введите аргумент №1 (от 0 до 9) ")
    var2 = input("Введите аргумент №2 (от 0 до 9) ")
    var3 = input("Введите аргумент №3 (от 0 до 9) ")
    args = var1 + var2 + var3
    args2 = args.replace(min(args), '')
    args3 = list(args2)
    return int(args3[0]) + int(args3[1])

print(my_func())

# хотел реализовать с 2-значными и более числами, но не получилось. Возникли сложности - либо можно применять мин/мах, но числа у нас склеиваются в одно типа не 20, 25, 30, а 202530,
# либо получаем список из [20, 25, 30], но не можем применить мин/мах

