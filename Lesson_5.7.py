# задание 7

import re
profit = {}
pr = {}
prof = 0
i = 0
prof_aver = 0
with open('file_8.txt', 'r', encoding = 'utf-8') as f_obj:
    for line in f_obj:
        a, b, c, d = line.split()
        profit[a] = int(c) - int(d)
        if profit.setdefault(a) >= 0:
            prof = prof + profit.setdefault(a)
            i += 1
            print(prof)
    if i != 0:
       prof_aver = prof/i
       print(pof_aver)

# если идти по пути работы со словарями (способы приведены в гугле), то из моего файла как будто цепляется только первая строка с положительной разностью 5000, остальные строки программа как будто не видит

