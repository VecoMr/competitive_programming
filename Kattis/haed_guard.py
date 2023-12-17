for i in open(0):
    i = i[:-1]
    t = 0
    m = None
    s = ""
    for j in i:
        if not m:
            t = 1
            m = j
            continue
        if m != j:
            s += str(t)+m
            t = 1
            m = j
        else:
            t += 1
    s += str(t)+m
    print(s)