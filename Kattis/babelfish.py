d = {}
t=True
for i in open(0):
    i = i.strip()
    if i == "":
        t = False
        continue
    if t:
        a,b = i.split()
        d[b] = a
    if not t:
        if not i in d:
            print("eh")
        else:
            print(d[i])