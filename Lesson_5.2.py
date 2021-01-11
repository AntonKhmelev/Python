# задание 2

my_file = open('file_2.txt', 'r')

lines = 0
words = 0
letters = 0

for line in my_file:
    lines += 1
    letters += len(line)
    pos = 'out'
    for letter in line:
        if letter != (' ') and pos == 'out':
           words += 1
           pos = 'in'
        elif letter == (' '):
           pos = 'out'

print(lines)
print(words)

