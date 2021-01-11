# задание 4

import json
import collections
import itertools


my_file = open('file_4.txt', 'r', encoding = 'utf-8')

my_str = my_file.read().split("\n")[:-1]

dict1 = dict()

for item in my_str:
    key = item.split(" ")[0]
    value = item.split(" ")[::-3]
    dict1[key] = value
print(dict1)

dict2 = {'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}

res = {}
res = {v:k for k,v in dict2.items()}
print(res)

p = []
q = []

for k,v in res.items():
    p.append(k)
for k,v in dict1.items():
    q.append(v)
print(p)
print(q)

t = dict(zip(p, q))
print(t)

string = []
for key, item in t.items():
    string.append("{}:{}".format(key.capitalize(), item))
result = ';''\n'.join(string)
print(result)

with open("file_5.txt", "w") as f_obj:
    print(result, file=f_obj)
