n,m = map(int,input().split())
d={}
for i in range(n):
    for j in input().split():
        d.setdefault(j,0)
        d[j]+=1
r=[]
for i in d:
    if d[i] == n:
        r.append(i)
print(len(r),*sorted(r),sep="\n")