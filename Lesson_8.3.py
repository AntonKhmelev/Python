# задание 3

class My_except():
    pass

a = []

while True:
    try:
        b = input("Введите числовое значение ")
        if b == "stop":
            break
        if not b.isdigit():
           raise ValueError(b)
        a.append(int(b))
    except ValueError as ex:
        print("Вы ввели нечисловое значение!", ex)
    else:
     pass
    finally:
     print(a)

