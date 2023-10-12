s, t, n = map(int,input().split())
d = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
z = [int(i) for i in input().split()]

while n:
    a, b, c = d.pop(0), l.pop(0), z.pop(0)
    n -= 1
    s += a
    if s%c:
        s += c - (s%c)
    s += b
s += d.pop(0)
if s <= t:
    print("yes")
else:
    print("no")