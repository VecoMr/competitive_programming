n = int(input())
for i in range(n):
    s = list(input())
    t = list(input())
    le = len(s)
    r = 0
    su = 0
    so = 0
    sz = 0
    for j in s:
        if j == "?":
            su += 1
        if j == "1":
            so += 1
        if j == "0":
            sz += 1
    tu = 0
    to = 0
    tz = 0
    for j in t:
        if j == "?":
            tu += 1
        if j == "1":
            to += 1
        if j == "0":
            tz += 1
    if so > to:
        print(f'Case {i+1}: -1')
        continue
    if so < to:
        for y in range(le):
            if t[y] == "1" and s[y] == "?":
                su -= 1
                so += 1
                s[y] = "1"
                r += 1
                if so == to:
                    break
    if so < to:
        for y in range(le):
            if t[y] == "1" and s[y] == "0":
                sz -= 1
                so += 1
                s[y] = "1"
                r += 1
                if so == to:
                    break
    for y in range(le):
        if s[y] == "?":
            r += 1
            s[y] = "0"
    print(*s,sep="")
    print(*t,sep="")
    r += sum(1 for i,j in zip(s,t) if i != j) // 2
    print(f'Case {i+1}: {r}')