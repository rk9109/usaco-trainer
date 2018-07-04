"""
ID: rk91091
LANG: PYTHON3
TASK: friday
"""

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')
N = int(fin.readline().strip())

month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count = [0, 0, 0, 0, 0, 0, 0]
day = 0

for i in range(1900, 1900 + N):
	month_list[1] = 28
	if (i % 400 == 0) or ((i % 4 == 0) and (i % 100 != 0)):
		month_list[1] = 29
	
	for month in month_list:
		for i in range(month):
			if i == 12:
				count[(day + 2) % 7] += 1
			day += 1

for i in range(7): count[i] = str(count[i])
fout.write(' '.join(count) + '\n')
fout.close()
