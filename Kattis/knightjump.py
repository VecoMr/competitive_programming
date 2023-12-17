import math
n = int(input())
l = [input() for _ in range(n)]
t = []

def e(l, lk, k, s, en, c, n):
    if c == en:
        return k
    m = math.inf
    if c:
        x, y = c
    else:
        x, y = s
    for i, j in [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1), (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]:
        if not (i,j) in lk and 0 <= i < n and 0 <= j < n and l[i][j] != "#":
            m = min(m, e(l, lk+[(i,j)], k+1, s, en, (i,j), n))
    return m

en = (0,0)
for i in range(n):
    for j in range(n):
        if l[i][j] == "K":
            s = (i,j)
            break
a = e(l, [], 0, s, en, s, n)
if a == math.inf:
    print(-1)
else:
    print(a)