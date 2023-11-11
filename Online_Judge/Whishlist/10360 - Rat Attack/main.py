n = int(input())

def calc(x, y, d, rat):
    return sum(i[2] for i in rat if x-d <= i[0] <= x+d and y-d <= i[1] <= y+d)

for _ in range(n):
    d = int(input())
    k = int(input())
    l = [list(map(int, input().split())) for _ in range(k)]
    m = 0
    t = (-1, -1)
    for i in range(1025):
        for j in range(1025):
            tmp = calc(i,j,d,l)
            if tmp > m:
                m = tmp
                t = (i,j)
    print(*t, m)