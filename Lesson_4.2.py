
# задача 2

import itertools
import functools


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123,55]
print(my_list)

a = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]

print(a)






