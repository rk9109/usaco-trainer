"""
ID: rk91091
LANG: PYTHON3
TASK: namenum
"""

fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w')

number = fin.readline().strip()

dict_ = {'A':2, 'B':2, 'C':2, 'D':3, 'E':3, 'F':3, 'G':4, 'H':4, 'I':4,
         'J':5, 'K':5, 'L':5, 'M':6, 'N':6, 'O':6, 'P':7, 'R':7, 'S':7,
         'T':8, 'U':8, 'V':8, 'W':9, 'X':9, 'Y':9, 'Q':0, 'Z':0}

names = open('dict.txt', 'r')

names_list = []
for i in range(5000):
    name = names.readline().strip()
    names_list.append(name)

names_dict = {}
for name in names_list:
    num = []
    for letter in name: num.append(str(dict_[letter]))
    num = ''.join(num)
    if num in names_dict.keys(): names_dict[num].append(name)
    else: names_dict[num] = [name]

try:
    valid_names = names_dict[number]
except KeyError:
    valid_names = ['NONE']

for name in valid_names:
    fout.write(name + '\n')
fout.close
