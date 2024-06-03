n = int(input())
l = [tuple(map(int,input().split())) for _ in range(n)]
for i in l:
    r, e, c = i
    if r + c == e:
        print("does not matter")
    elif r + c > e:
        print("do not advertise")
    else:
        print("advertise")