n = int(input())
for _ in range(n):
    l = input().split()
    a,b=(0,0)
    r = []
    for i in l:
        if a and b:
            r.append(i)
        else:
            if i == "Simon":
                a = 1
            else:
                if i == "says" and a == 1:
                    b = 1
                else:
                    a,b= 0,0
    if r:
        print(*r)