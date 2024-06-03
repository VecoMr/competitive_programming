d = {}

for i in open(0):
    a, *b = i.strip().split()
    if a == "clear":
        d = {}
    elif a == "def":
        d[b[0]] = int(b[1])
    else:
        if (sum(1 for j in b if not j in "+-/*=" and not j in d)):
            print(" ".join(b), "unknown")
        else:
            tmp = eval(" ".join(str(d[j]) if j in d else j for j in b[:-1]))
            t = "unknown"
            for i in d:
                if d[i] == tmp:
                    t = i
                    break
            print(" ".join(b), t)