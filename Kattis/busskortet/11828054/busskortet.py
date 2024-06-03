import math
n = int(input())
l = [500, 200, 100]
r = 0
for i in l:
    r += n//i
    n -= (n//i)*i
print(r)