n = int(input())
for _ in range(n):
    m = int(input())
    l = []
    a, b = 1, 1
    i = 1
    # while not a in l:
    #     l.append(a)
    #     a, b = (a+b)%m, a
    #     i+=1
    for i in range(15):
        l.append(a%m)
        a, b = (a+b), a
    print(l, a, b)
    print(i)
