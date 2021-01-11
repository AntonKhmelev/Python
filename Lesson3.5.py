# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# задание 5

def my_func():
    my_sum = 0
    a = False
    while a == False:
        num = input("Введите числа, разделенные пробелом ").split()

        i = 0
        for el in range(len(num)):
            if num[el] == '$':
            a = True
            break
        else:
            i = i + int(num[el])
            my_sum = my_sum + i
            return my_sum

print(my_func())

# где-то ошибка, то ли в отступах, то ли в синтаксисе, не могу понять










