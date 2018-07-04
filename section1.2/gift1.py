"""
ID: rk91091
LANG: PYTHON3
TASK: gift1
"""
fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

num_people = int(fin.readline().strip())
dict_ = {}
list_ = []

for i in range(num_people):
	name = fin.readline().strip()
	dict_[name] = 0
	list_.append(name)

for i in range(num_people):
	giver = fin.readline().strip()
	money, num = map(int, fin.readline().split())
	
	if (num != 0): dict_[giver] -= (money//num)*num
	else: dict_[giver] += money

	for i in range(num):
		receiver = fin.readline().strip()
		dict_[receiver] += (money//num)

for name in list_:
	fout.write(name + ' ' + str(dict_[name]) + '\n')
fout.close()
