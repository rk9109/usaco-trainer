"""
ID: rk91091
LANG: PYTHON3
TASK: palsquare
"""

fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')

base = int(fin.readline().strip())

dict_ = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
         10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I',
         19:'J', 20:'K'}

# Function to convert base
def convert_base(num, base):
    digits = []; first = False
    for i in range(20, -1, -1):
        counter = 0
        while num > 0:
            if (num - base**i) >= 0:
                num = num - base**i
                first = True
                counter += 1
            else: break
        if first: digits.append(dict_[counter])
    return digits

# Function to check palindrome
def check_palindrome(digits):
    initial = 0; final = -1
    for i in range(len(digits)):
        if digits[initial] == digits[final]:
            initial += 1
            final -= 1
        else:
            return False
    return True

for i in range(1, 301):
    digits_squared = convert_base(i**2, base)
    if check_palindrome(digits_squared):
        digits = convert_base(i, base)
        digits_squared = ''.join(digits_squared)
        digits = ''.join(digits)
        fout.write(digits + ' ' + digits_squared + '\n')
fout.close()
