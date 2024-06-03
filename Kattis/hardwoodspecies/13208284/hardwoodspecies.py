l = [i.strip() for i in open(0)]
n = 0

d = {}
for i in l:
    d.setdefault(i, 0)
    d[i] += 1
    n += 1

for i in sorted([(i, d[i]/n*100) for i in d]):
    print(*i)