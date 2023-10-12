input()
nl = sorted(map(int, input().split()))
ml = map(int, input().split())
d = {}
r = []
for i in ml:
    if not i in d:
        d[i] = sum(nl[:i])
    r.append(d[i])
print(*r,sep="\n")