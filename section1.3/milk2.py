"""
ID: rk91091
LANG: PYTHON3
TASK: milk2
"""

fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

num = int(fin.readline().strip()

list_ = []
for i in range(5000):
	list_.append(0)

for i in range(num):
	start, end = map(int, fin.readline().split())
	list_[start:end] = [1]*(end - start)

max_continuous = []
max_idle = []
continuous = 0
idle = 0
value = 0

for v in list_:
	if v == value:


