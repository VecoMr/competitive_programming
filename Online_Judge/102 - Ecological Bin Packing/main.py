for i in open(0):
    l = list(map(int, i.split()))
    su = sum(l)
    a = l[0] + l[4] + l[8]
    b = l[0] + l[5] + l[7]

    c = l[1] + l[3] + l[8]
    d = l[1] + l[5] + l[6]

    e = l[2] + l[3] + l[7]
    f = l[2] + l[4] + l[6]

    ma = max(a, b, c, d, e, f)

    if b == ma:
        print("BCG", su -b)
    elif a == ma:
        print("BGC", su - a)
    elif e == ma:
        print("CBG", su - e)
    elif f == ma:
        print("CGB", su -f)
    elif c == ma:
        print("GBC", su - c)
    elif d == ma:
        print("GCB", su - d)