import math

n = int(input())
l = [input().split() for i in range(n)]
l = [[i[0], float(i[1]), float(i[2])] for i in l]
a = sorted(l, key=lambda x: x[1])[:4]
b = sorted(l, key=lambda x: x[2])[:4]

m = math.inf
t = []
for i in range(4):
    tm = [a[i]]
    for j in range(4):
        if not b[j][0] == a[i][0]:
            tm.append(b[j])
    if sum(j[2] for j in tm[1:4]) + tm[0][1] < m:
        t = tm[:4]
        m = sum(j[2] for j in tm[1:4]) + tm[0][1]
print(m, *[i[0] for i in t],sep="\n")


