n,m=map(int,input().split())
l=list(map(int,input().split()))
res = 0
for _ in range(m):
    i = l.pop(0)
    if n - i < 0:
        res += 1
    else:
        n -= i
print(res)

