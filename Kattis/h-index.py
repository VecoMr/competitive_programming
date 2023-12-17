n, *l = map(int, open(0))
l.append(0)
g = sorted(set(l), reverse=True)
lg = len(g)
print(n,l, g)
m = 0
for i in range(1, lg):
    print([1 for j in l if j >= g[i]])
    if g[i] <= sum(1 for j in l if j >= g[i]):
        print(g[i],  g[i - 1])
        for j in range(g[i], g[i - 1]):
            if j >= sum(1 for a in l if a >= g[i]):
                m = j
            else:
                break
        print(m)
        break


