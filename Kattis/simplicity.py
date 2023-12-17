s=input()
l = sorted([[s.count(i), i] for i in set(s)])
r = 0
while len(l) > 2:
    r += l.pop(0)[0]
print(r)