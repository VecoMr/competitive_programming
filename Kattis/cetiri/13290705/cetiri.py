l=sorted(map(int,input().split()))
a,b = l[1] - l[0], l[2] - l[1]
if a == b:
    print(l[2]+a)
elif a < b:
    print(l[1]+b//2)
elif a > b:
    print(l[0]+a//2)