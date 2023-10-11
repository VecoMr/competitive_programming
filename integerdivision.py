n,d=map(int,input().split())
l=list(map(int,input().split()))
f = {}
for i in l:
    if i//d in f:
        f[i//d] += 1
    else:
        f[i//d] = 1
print(sum(sum(j for j in range(f[i])) for i in f))