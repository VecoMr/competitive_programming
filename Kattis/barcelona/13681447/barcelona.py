n,m=map(int,input().split())
l=list(map(int,input().split()))
if n == 1 or l[0] == m:
    print("fyrst")
else:
    if l[1] == m:
        print("naestfyrst")
    else:
        print(l.index(m)+1,"fyrst")