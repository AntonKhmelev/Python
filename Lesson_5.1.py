# задание 1

lines = []
a = input("Введите содержание строки ")

while a != (''):
    a = input("Введите содержание строки ")
    lines.append(a)


with open("file_1.txt", "w") as file:
    for line in lines:
        file.write(line + '\n')

