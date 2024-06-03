t,b = map(int,input().split())
store = list(map(int, input().split()))
d = {i:int(j) for i,j in [input().split() for _ in range(t)]}
for i in store:
    res = 0
    for _ in range(i):
        a, b = input().split()
        res += d[a] - int(b)
    print(res)