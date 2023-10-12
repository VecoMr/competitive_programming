import math
def calc(a, b, c, d, e, f):
    det = (a*d-b*c)
    if det == 0:
        return (-math.inf, -math.inf)
    return ((e*d-b*f)/det, (a*f-e*c)/det)

for i in open(0):
    d,p,*l=map(int, i.split())
    if p < l[0]:
        print("The spider is going to fall!")
        continue
    le = len(l)
    if d != le-1:
        a,b,c,v = l[-4:]
        x, y = calc(a,b,b,c,c,v)
        if x == -math.inf or y == -math.inf:
            for i in range(d-le+1):
                l.append(x)
        else:
            for i in range(d-le+1):
                l.append(l[-2]*x+l[-1]*y)
                if l[-2]*x+l[-1]*y > p:
                    break
    index = 0
    for i in l:
        if i > p:
            break
        index += 1
    if index == d+1:
        print("The spider may fall!")
        continue
    print(d+1-index)