l = [input().split() for _ in "aaa"]
a,b = False, False

def e(c,t):
    return (t, c)[t == "_"]

for i in range(3):
    for j in range(3):
        c = l[i][j]
        if c != "_":
            if c == e(c,l[(i-1)%3][j]) == e(c,l[(i-2)%3][j]) or c == e(c,l[i][(j-1)%3]) == e(c,l[i][(j-2)%3]):
                if c == "X":
                    a = True
                else:
                    b = True
        else:
            if e(c,l[(i-1)%3][j]) == e(c,l[(i-2)%3][j]) or e(c,l[i][(j-1)%3]) == e(c,l[i][(j-2)%3]) or (e(c,l[(i-1)%3][j]) == "_" or e(c,l[(i-2)%3][j]) == "_" or e(c,l[i][(j-1)%3]) == "_" or e(c,l[i][(j-2)%3]) == "_"):
                a
            