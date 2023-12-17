q, a, b = map(int, input().split())

def all_div(a, b):
    l = []
    r = 1
    while a * r <= b:
        if b % (a * r) == 0:
            l.append(r)
        r += 1
    return l[::-1]
ind = (0, 1)

if a < b:
    a, b = b, a
    ind = (1, 0)

print(all_div(a, q))

for i in all_div(a, q):
    print(i, (q - (i * a)) % b)
    if (q - (i * a)) % b == 0 and (q - (i * a))//b >= 0:
        print((i, (q - (i * a))//b)[ind[0]], (i, (q - (i * a)))[ind[1]])
        exit()
print("impossible")