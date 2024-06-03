n,m = map(int,input().split())
l = [input() for _ in range(n)]
allWorlds = []
for i in l:
    allWorlds.extend(j for j in i.split("#") if j and len(j) > 1)
for i in list("".join(i) for i in zip(*l)):
    allWorlds.extend(j for j in i.split("#") if j and len(j) > 1)
print(sorted(allWorlds)[0])