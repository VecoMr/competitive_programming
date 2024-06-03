n,m=map(int,input().split())
l=sorted(map(int,input().split()),reverse=True)
d=n-m
if d <= 0:
    print(max(l[:abs(d)+1]))
else:
    md=m%n
    tt = d*2
    ma = 0
    if n-tt > 0:
        ma = max(l[:n-tt])
        del l[:n-tt]

    ma = max(ma, max(l[i]+l[-i-1] for i in range(len(l)//2)))
    print(ma)