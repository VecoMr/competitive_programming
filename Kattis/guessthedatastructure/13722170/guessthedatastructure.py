l = [i[:-1] for i in open(0)]
le = len(l)
i = 0
while i < le:
    n = int(l[i])
    i += 1
    lt = [list(map(int, l[i+j].split())) for j in range(n)]
    i += n
    tmpQ = []
    tmpS = []
    tmpP = []
    q = True
    p = True
    s = True
    imp = False
    size = 0
    for a, j in lt:
        if a == 1:
            size += 1
            if q: tmpQ.append(j)
            if p: tmpP.append(j)
            if s: tmpS.append(j)
        else:
            if size < 1:
                imp = True
                break
            if p and max(tmpP) != j:
                p = False
            else:
                if p: tmpP.remove(j)
            if q and tmpQ[0] != j:
                q = False
            else:
                if q: del tmpQ[0]
            if s and tmpS[-1] != j:
                s = False
            else:
                if s: del tmpS[-1]
            size -= 1
            if not (s or q or p):
                break
    if imp:
        print("impossible")
        continue
    if (q + p + s) > 1:
        print("not sure")
    elif q:
        print("queue")
    elif s:
        print("stack")
    elif p:
        print("priority queue")
    else:
        print("impossible")


