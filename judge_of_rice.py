n = int(input())
s = int(input() != "antal")
l = []
for i in range(n):
    t = list(map(int,input().split()))
    t.append(i)
    l.append(t)
l = sorted(l, key=lambda x: (x[0]+x[1], x[s]))
print(l[-1][2]+1)