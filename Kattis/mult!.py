n,*l=map(int,open(0))
d = None
while l:
    a = l.pop(0)
    if d == None:
        d = a
        continue
    if a%d == 0:
        print(a)
        d=None
