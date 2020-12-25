# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# задание 1

def div():
    try:
      global var1, var2, var3
      var1 = input("Введите делимое ")
      var2 = input("Введите делитель ")
      var3 = int(var1) / int(var2)
    except ZeroDivisionError:
      return
    return var3

print(f" Частное от деления {'введенного делимого'} на {'введенное частное'} составляет {div()}")
# введение global не помогло print в f-строке увидеть переменные var1 и var2 из тела функции, хотя в примере из методички это получается