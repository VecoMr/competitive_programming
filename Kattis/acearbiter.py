n = int(input())
l = [tuple(map(int, input().split("-"))) for _ in range(n)]
tmp = l.pop(0)
r = 1
t = False
tour = 1
t_p = 0

while l:
    i = l.pop(0)
    if t_p == 1:
        i = (i[1], i[0])
    if i == tmp:
        if t:
            print(f"Error {r}")
            break
        else:
            t = True
    else:
        t = False
    