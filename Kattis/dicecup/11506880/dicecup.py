a,b=map(int,input().split())
d = {}
for i in range(1,a+1):
    for j in range(1,b+1):
        if i+j not in d:
            d[i+j] = 1
        else:
            d[i+j] += 1
l = sorted((d[i], i) for i in d)[-1][1]
l = sorted([i for i in d if d[i] == d[l]])
print(*l, sep="\n")