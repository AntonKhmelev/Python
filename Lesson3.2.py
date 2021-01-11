# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# задание 2

def func(name, surn, birth, city, email, tel):
    card = (f"{name}, {surn}, {birth}, {city}, {email}, {tel}")
    return card

print(func(name = 'Anton', email = 'khmeleov@mail.ru', surn = 'Khmelev', tel = '8903...', birth = 'December 87', city = 'Moscow'))
