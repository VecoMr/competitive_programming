s = input()
e = int(input())
le = [input().split() for _ in range(e)]
p = int(input())
lp = [input().split() for _ in range(p)]
lle = []
for i in le:
    for j in i:
        if s.endswith(j):
            lle.extend(i)
lle = set(lle)
for j in lp:
    a = False
    for i in lle:
        if j[-1].endswith(i):
            a = True
            break
    print(("NO","YES")[a])
