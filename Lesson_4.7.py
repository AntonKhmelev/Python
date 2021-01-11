
# задача 7

def fact(n):
    i = 1
    for el in range(1, n + 1):
        i = i * el
        yield i

for el in fact(5):
    print(el)


















