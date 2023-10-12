n,m = map(int,input().split())
l = sorted(map(int,input().split()))
r = min(n,1)
for i in range(1, n):
    if l[i]+l[i-1] <= m:
        r+=1
    else:
        break
print(r)