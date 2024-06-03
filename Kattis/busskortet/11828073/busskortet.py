import math
n = int(input())
l = [500, 200, 100]
res = []
r = 0
for i in l:
    r += n//i
    n -= (n//i)*i
    res.append([n-i, r+1])
print(min(res, key=lambda x: (-x[0], x[1]))[1])