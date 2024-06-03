n = int(input())

cube = []
cylinder = []

for _ in range(n):
    a,b=input().split()
    (cube, cylinder)[a == "cylinder"].append(int(b))

cube.sort(reverse=True)
cylinder.sort(reverse=True)

t = True
tmp = float("inf")
type = "cube"

def isPossible(a, b):
    ta, sa = a
    tb, sb = b
    if ta == tb:
        return sa >= sb
    if ta == "cube":
        return sa >= sb*2
    return (((sa**2)/2)**0.5)*2 >= sb

r = []

for i in range(n):
    cy = False
    cu = False
    a = cylinder[0] if cylinder else None
    cy = a and isPossible((type, tmp), ("cylinder", a))
    b = cube[0] if cube else None
    cu = b and isPossible((type, tmp), ("cube", b))
    
    if cy and cu:
        if isPossible(("cylinder", a), ("cube", b)):
            type = "cylinder"
            tmp = a
            cylinder.pop(0)
            r.append(f'{type} {tmp}')
            continue
        type = "cube"
        tmp = b
        r.append(f'{type} {tmp}')
        cube.pop(0)
        continue
    elif cy:
        type = "cylinder"
        tmp = a
        cylinder.pop(0)
        r.append(f'{type} {tmp}')
        continue
    elif cu:
        type = "cube"
        tmp = b
        r.append(f'{type} {tmp}')
        cube.pop(0)
        continue
    t = False
    break



if t:
    print(*r[::-1],sep="\n")
else:
    print("impossible")