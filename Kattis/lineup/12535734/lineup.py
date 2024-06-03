n,*l=open(0)
s=sorted(l)
i,d=True,True
n=int(n)
for y in range(n):
    if l[y] != s[y]:
        i=False
    if l[n-y-1] != s[y]:
        d=False
if d:
    print("DECREASING")
elif i:
    print("INCREASING")
else:
    print("NEITHER")