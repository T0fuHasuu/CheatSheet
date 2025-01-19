def Modulo(n, m):
    remainder = 0
    for digit in n:
        remainder = (remainder * 10 + int(digit)) % m
    return remainder

import sys
line = sys.stdin.readline().strip()
n, m = line.split()
m = int(m)

print(Modulo(n, m))