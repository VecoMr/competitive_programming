n = int(input())
l = [input() for _ in range(n)]
m = int(input())
for _ in range(m):
    act, *arg = input().split()
    if act == "cut":
        l.insert(l.index(arg[1]), arg[0])
    else:
        l.remove(arg[0])
print(*l,sep="\n")