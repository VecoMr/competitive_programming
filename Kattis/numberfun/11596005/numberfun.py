n = int(input())
for _ in range(n):
    l = list(map(int,input().split()))
    t = False
    for i in range(3):
        a,b,c = l[i:] + l[:i]
        if a+b == c or a-b == c or (b and a/b == c) or a*b == c:
            t = True
            break
    if t:
        print("Possible")
    else:
        print("Impossible")