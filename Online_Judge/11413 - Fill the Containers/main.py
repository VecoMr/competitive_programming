import math
l = [list(map(int, i.split())) for i in open(0)]

def is_possible(m, l, c):
    r = [0]*m
    k = 0
    t = []
    for i in l:
        if r[k] + i > c:
            t.append(r[k]+i - c)
            k += 1
            if k >= m:
                return min(t)
        r[k] += i
    return False

for i in range(0,len(l),2):
    n, m = l[i]
    milks = l[i+1]
    c = max(math.ceil(sum(milks)/m), max(milks))
    a = 0
    while a := is_possibble(m, milks, c):
        # print(a)
        c += a
    print(c)