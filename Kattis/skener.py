r, c ,zr, zc = map(int,input().split())
l = [list(input()) for _ in range(r)]
for i in range(r):
    s = ""
    for j in range(c):
        for b in range(zc):
            s += l[i][j]
    for a in range(zr):
        print(s)
