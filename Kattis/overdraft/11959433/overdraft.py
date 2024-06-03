n,*l=map(int,open(0))
r=0
b=0
for i in l:
    b += i
    r = min(r,b)
print(abs(r))