t, s, _ = map(int,input().split())
l = list(map(int,input().split()))
a = 0
b = s
last = l[0]
for i in l:
    if i > t:
        break
    d = i - last
    tb = max(0, a-d)
    ta = min(s, b+d)
    b = tb
    a = ta
    last = i

print(max(0, a - (t - last)))
