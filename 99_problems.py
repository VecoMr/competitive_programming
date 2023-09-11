n, q = map(int, input().split())
l = sorted(list(map(int, input().split())))
for _ in range(q):
    s, i = map(int, input().split())
    if s == 1:
        t = True
        for j in range(n):
            if l[j] > i:
                print(l.pop(j))
                n -= 1
                t = False
                break
        if t:
            print(-1)
    elif s == 2:
        t = True
        for j in range(n-1, -1, -1):
            if l[j] <= i:
                print(l.pop(j))
                n -= 1
                t = False
                break
        if t:
            print(-1)