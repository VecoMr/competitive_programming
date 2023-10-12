a,b,c=map(int,input().split())
r=0
while abs(a-b) > 1 or abs(b-c) > 1:
    r+=1
    if abs(a-b) > abs(b-c):
        c = (a+b)//2
    else:
        a = (c+b)//2
    a,b,c = sorted([a,b,c])
    print(a,b,c)
print(r)