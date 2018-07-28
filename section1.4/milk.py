"""
ID: rk91091
LANG: PYTHON3
TASK: milk
"""

fin = open('milk.in', 'r')
fout = open('milk.out', 'w')

price_dict = {}

N, M = map(int, fin.readline().split())
for i in range(M):
    P, A = map(int, fin.readline().split())
    if P in price_dict.keys(): price_dict[P] += A
    else: price_dict[P] = A

# Calculate cost
def calculate_cost(N, price_dict):
    cost = 0
    if N == 0: return 0
    for key in sorted(price_dict.keys()):
        if N - price_dict[key] > 0:
            cost += key*price_dict[key]
            N -= price_dict[key]
        else:
            for i in range(price_dict[key] + 1):
                if N - i == 0:
                    cost += key*i
                    return cost

fout.write(str(calculate_cost(N, price_dict)) + '\n')
fout.close()
