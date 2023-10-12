l, d, x = map(int, open(0))
for i in range(l, d+1):
    if sum(map(int,str(i))) == x:
        print(i)
        break
for i in range(d, l-1, -1):
    if sum(map(int,str(i))) == x:
        print(i)
        break
