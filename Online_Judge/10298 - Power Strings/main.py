s = input()

while s != ".":
    r = 1
    le = len(s)
    t = True
    while t:
        if le%r == 0:
            tmp = False
            for i in range(0, le-r+1, r):
                if s[0:r] != s[i:i+r]:
                    tmp = True
                    break
            if tmp:
                r += 1
                continue
            t = False
        else:
            r += 1
    print(le//r)
    s = input()