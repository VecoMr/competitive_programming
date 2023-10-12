
for i in map(int,open(0)):
    t = 0
    n = 1
    while n < i:
        n *= 9
        t += 1
    print(n,t)