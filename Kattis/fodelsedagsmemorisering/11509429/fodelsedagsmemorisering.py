n = int(input())
l = [input().split() for _ in range(n)]
d = {}
for i in l:
    if not i[2] in d:
        d[i[2]] = (int(i[1]), i[0])
    else:
        if d[i[2]][0] < int(i[1]):
            d[i[2]] = (int(i[1]), i[0])
print(*sorted([d[i][1] for i in d]), sep="\n")