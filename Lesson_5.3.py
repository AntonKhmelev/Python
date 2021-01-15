# задание 3
from itertools import groupby
from operator import itemgetter
import ast



my_file = open('file_3.txt', 'r', encoding = 'utf-8')

my_str = my_file.read().split("\n")[:]

dict = dict()

for item in my_str:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    dict[key] = value

print(dict)

for i in sorted(dict.items(), key = lambda x: (x[1], x[0])):
    print(i)

with open ('file_3.txt', 'r', encoding = 'utf-8') as file:
    man = {}
    for line in file:
        key, value = line.split()
        man[key] = value
        if float(value) < 20000:
            print({key})

# не догадался, как вывести среднее
