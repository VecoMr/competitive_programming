k,q = map(int,input().split())
d = [0]*k
for _ in range(q):
    a,b = map(int,input().split())
    d[b-1] += 1
print(min(d))