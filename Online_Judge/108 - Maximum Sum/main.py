import math
n,*tmp_l=open(0)
n = int(n)
l = []
for i in tmp_l:
    l.extend(list(map(int, i.split())))
tmp_l = l
l = []
for i in range(n):
    l.append(tmp_l[i*n:(i+1)*n])

r = -math.inf

for i in range(n):
    for j in range(n):
        k = [0]*n
        for y in range(i, n):
            s = 0
            for x in range(j, n):
                s += l[y][x]
                if s+sum(k[:x+1]) > r:
                    r = s+sum(k[:x+1])
            for x in range(j, n):
                k[x] += l[y][x]
print(r)
