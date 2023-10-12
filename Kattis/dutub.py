import math

n = int(input())
l = [[int(i), j] for i,j in [input().split() for _ in range(n)]]
d = {}

def func(cur, l, need):
    if not need:
        return sum(l[i][0] for i in cur)
    m = math.inf
    for j in range(n):
        if not j in cur:
            if sum(1 for i in l[j][1] if i in need):
                s = "".join(sorted(str(i) for i in cur+[j]))
                if not s in d:
                    d[s] = func(cur+[j], l, "".join(i for i in need if i not in l[j][1]))
                m = min(m, d[s])
    return m


print(func([], l, set("".join(i[1] for i in l))))