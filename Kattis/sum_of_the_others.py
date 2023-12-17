for i in open(0):
    l = list(map(int,i.split()))
    s = sum(l)
    for i in set(l):
        if i == s - i:
            print(i)