l = list(map(int,open(0)))
a = l[:]
d = {}
for j in l:
    d[j] = 0
for i in range(1, max(l)//2+1):
    t = []
    for j in l:
        if j%i == 0:
            print(d[j], j , i)
            d[j] += i
            if d[j] - j > 2:
                t.append(i)
        if j < i//2:
            t.append(i)
    for j in set(t):
        l.remove(j)

print(a, d)
for i in a:
    if d[i] == i:
        print(f"{i} perfect")
    elif abs(d[i] - i) <= 2:
        print(f"{i} almost perfect")
    else:
        print(f"{i} no perfect")