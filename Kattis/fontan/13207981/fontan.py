n,m=map(int,input().split())
l = [list(input()) for _ in range(n)]

for i in range(n-1):
    for j in range(m):
        if l[i][j] == "V":
            for k in range(j, m):
                if l[i][k] == "#":
                    break
                if l[i+1][k] == "#":
                    l[i][k] = "V"
                else:
                    l[i][k] = "V"
                    l[i+1][k] = "V"
                    break
            for k in range(j, -1, -1):
                if l[i][k] == "#":
                    break
                if l[i+1][k] == "#":
                    l[i][k] = "V"
                else:
                    l[i][k] = "V"
                    l[i+1][k] = "V"
                    break

print(*["".join(i) for i in l],sep="\n")