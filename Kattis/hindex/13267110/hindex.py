n,*l=map(int,open(0))
l.sort(reverse=True)
r=0
for i in range(n):
 if l[i] < i+1:break
 r = i+1
print(r)