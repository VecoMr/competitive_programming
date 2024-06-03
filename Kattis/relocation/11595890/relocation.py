n, q = map(int,input().split())
d = {}
for i, j in enumerate([int(i) for i in input().split()]):
    d[i] = j



for _ in range(q):
    m, a, b = map(int, input().split())
    if m == 1:
        d[a-1] = b
    elif m == 2:
        print(abs(d[a-1] - d[b-1]))