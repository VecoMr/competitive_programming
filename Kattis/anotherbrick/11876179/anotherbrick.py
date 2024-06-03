h,w, n = map(int,input().split())
l = list(map(int, input().split()))
t = w
tm = True
while h and l:
    i = l.pop(0)
    t -= i
    if t < 0:
        tm = False
        break
    if t == 0:
        t = w
        h -= 1


if not tm or h != 0:
    print("NO")
else:
    print("YES")