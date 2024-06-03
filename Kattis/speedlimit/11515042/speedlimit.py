s = int(input())
while s != -1:
    l = [list(map(int,input().split())) for _ in range(s)]
    s = int(input())
    t = 0 
    r = 0
    for i in l:
        a,b = i
        b, t = b-t, b
        r += a*b
    print(r, "miles")


