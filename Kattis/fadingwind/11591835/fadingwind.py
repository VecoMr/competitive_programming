h, k, v, s = map(int,input().split())
r = 0
while h > 0:
    v += s
    v -= max(int(v/10), 1)
    if v >= k:
        h += 1
    if 0 < v < k:
        h -= 1
        if h == 0:
            v = 0
    if v <= 0:
        h = 0
        v = 0
    r += v
    if s > 0:
        s -= 1
print(r)