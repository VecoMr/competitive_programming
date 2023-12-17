n, m = map(int, input().split())
while n or m:
    d = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        d[b].append(a)
    l = list(range(1,n+1))
    r = []
    while len(r) != n:
        for i in range(1, 1+n):
            if not d[i] and not i in r:
                r.append(i)
                for j in range(1, 1+n):
                    if i in d[j]:
                        d[j].remove(i)
                break
    print(*r)
    n, m = map(int, input().split())