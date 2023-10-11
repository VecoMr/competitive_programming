d = []

for i in open(0):
    l = i[:-1].split()
    r = []
    for j in l:
        if j.lower() in d:
            r.append(".")
        else:
            d.append(j.lower())
            r.append(j)
    print(*r)
