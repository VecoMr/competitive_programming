n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
r = []
for i in range(n):
    for j in range(n):
        if l[i][j] != -1:
            r.append([str(i+1), str(j+1), str(l[i][j])])
print(len(r))
print(*[" ".joint(i) for i in r], sep="\n")