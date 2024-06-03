n=int(input())
l=sorted(list(map(int,input().split()))for _ in range(n))
s,e=l.pop(0)
r=0
for i,j in l:
    if i >= s and i <= e:
        e = max(e, j)
    else:
        r += e-s+1
        s = i
        e = j
r += e-s+1
print(r)