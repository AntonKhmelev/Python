
# задача 6
from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)


i = 0
for el in cycle(' С Новым 2021 годом!'):
    if i > 12:
        break
    else:
        print(el)
        i += 1
















