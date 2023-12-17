import math

for i in open(0):
    *l,_ = map(int, i.split())
    le = len(l)
    m = -math.inf
    tmp = 0
    for i in range(le):
        tmp = 1
        for j in range(i,le):
            tmp *= l[j]
            if tmp > m:
                m = tmp
    print(m)
