n = int(input())
l = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[0], abs(x[0] - x[1])), reverse=True)
r = []
res = 0
for i in l:
    re = False
    a, b = i
    for j in r:
        c, d = j
        if c <= a <= d  or c <= b <= d:
            re = True
            break
    if not re:
        r.append(i)
        res += 1
print(res)