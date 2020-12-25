# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# задание 4

def my_func():
    x = abs(complex(input("Введите число ")))
    y = int(input("Введите степень "))
    #a = x ** y # реализация для **
    #return a

#print(my_func())
    i = 1
    n = 1
    k = 1
    j = 1

    while i <= y:
         n *= x
         i += 1
         return n
    #elif i > y:
     #     n *= 1/x
      #    i -= 1
       #   return n
    #else:
    #pass

    # не смог реализовать для Y < 0, кажется, цикл с условия elif i > y перестает прокручиваться более чем на 1 шаг

print(my_func())








