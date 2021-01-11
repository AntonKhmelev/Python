
# задача 5
import collections
from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]
a = reduce(lambda x, y: x * y, my_list)
print(my_list)
print(a)
















