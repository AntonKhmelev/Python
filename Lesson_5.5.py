# задание 5


my_file = open('file_6.txt', 'w', encoding = 'utf-8')
a = input("Введите числа через пробел ")
b = my_file.write(a)
nums = a.split()
print(nums)

nums2 = [int(x) for x in nums]
print(nums2)

summ = 0
for x in nums2:
    summ += x

print(summ)