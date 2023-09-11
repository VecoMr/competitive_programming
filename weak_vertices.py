n = int(input())
while n != -1:
    l = [list(map(int, input().split())) for _ in range(n)]
    r = []
    for i in range(n):
        for j in range(n):
            if j != i and l[i][j]:
                for a in range(n):
                    if a != j and a != i and l[i][a] and l[a][j]:
                        r.append(i)
                        break
            if i in r:
                break
    print(*[i for i in range(n) if i not in r])
    n = int(input())