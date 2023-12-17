n,*l=map(int,open(0))
l.sort(reverse=True)
r=0
for i in range(n):
    if l[i] >= i+1:
        r = i+1
    else:
        break
print(r)