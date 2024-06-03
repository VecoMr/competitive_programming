a,b,c=sorted(map(int,input().split()))
r=0
while c-a > 2:
    if b-a < c-b:
        a=b+1
    else:
        c=b-1
    a,b,c=sorted([a,b,c])
    r+=1
print(r)