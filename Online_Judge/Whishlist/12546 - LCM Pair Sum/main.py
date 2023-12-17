n = int(input())
for _ in range(n):
    m = int(input())
    r = 0
    nb = 1
    l = [nb]
    for _ in range(m):
        a, b = map(int, input().split())
        for i in range(b):
            for j in range(len(l)):
                l.append(l[j]*a)
    l = list(set(l))
    r = 0
    le = len(l)
    m = l[-1]
    for i in range(le):
        for j in range(i, le):
            if l[i] * l[j] >= m and (l[j] ):
                r += l[i]+l[j]
                print(l[i], l[j])
    print(r)

