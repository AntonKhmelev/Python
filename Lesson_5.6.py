# задание 6

import re

my_dict = {}

my_file = open('file_7.txt', 'r', encoding = 'utf-8')
g = 0
h = []
nums = []
for line in my_file:
    h = re.findall("\d+",line)
    k = nums.append(h)#sum([int(item) for item in h])
    #print(sum(nums))
    g += 1
print(nums)

total = 0
my_new_list = []
for sublist in nums:
    total = sublist[1] + total
    new_list = [sublist[0], total]
    my_new_list.append(new_list)
print(my_new_list)

#print(nums)
#l = dict.fromkeys(b)

#v_nums = []
       #   for v in l.keys():
        #   v_nums.append(v)
         #  print(v_nums)

my_file = open('file_7.txt', 'r', encoding = 'utf-8')

my_str = my_file.read().split("\n")[:]

dict1 = dict()

for item in my_str:
  key = item.split(" ")[0]
  value = item.split(" ")[1:]
  dict1[key] = value
print(dict1)

v_nums2 = []
for v in dict1.keys():
    v_nums2.append(v)
print(v_nums2)


# получил список списков чисел типа [[120, 34. 56], [34, 56], [20]] - не удалось сложить подсписки чисел, чтобы присовокупить полученные суммы элементов списка к ключам словаря
