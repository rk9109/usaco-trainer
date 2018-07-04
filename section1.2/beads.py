"""
ID: rk91091
LANG: PYTHON3
TASK: beads
"""

fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

num = int(fin.readline().strip())
beads = fin.readline().strip()

count = [['x', 0]] # placeholder

for bead in beads:
	if count[-1][0] == bead:
		count[-1][1] += 1
	else: count.append([bead, 1])

count.remove(['x', 0]) # remove placeholder		
lengths = []

if len(count) == 1:
	lengths.append(count[0][1])

else:
	for i in range(len(count)):
		length = 0
		index = i
		truth = [True, count[i][0]]
		
		if (truth[1] == 'w'): 
			if (i + 1 == len(count)): truth[1] = count[0][0]
			else: truth[1] = count[i + 1][0]
		
		for j in range(len(count)):
			if (index == len(count)): index = 0

			color = count[index][0]
			if (color != truth[1]) and (color != 'w') and (truth[0] == True):
				truth[0] = False
				truth[1] = color

			if (color != truth[1]) and (color != 'w') and (truth[0] != True): 
				break
				
			length += count[index][1]
			index += 1
			
		lengths.append(length)

fout.write(str(max(lengths)) + '\n')
fout.close()
