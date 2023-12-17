s = input()
i = 1
while s != "END":
    l = s.split("*")[1:-1]
    if l :
        a = len(l[0])
        b = sum(1 for i in l if len(i) != a)
        if b:
            print(i, "NOT EVEN")
        else:
            print(i, "EVEN")
    else:
        print(i,"EVEN")
    i+=1
    s = input()