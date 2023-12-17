def nb_cycle(n):
    r = 1
    while n != 1:
        if n%2==0:
            n//=2
        else:
            n=n*3+1
        r+=1
    return r

for i in open(0):
    x, y = map(int, i.split())
    i,j = min(x,y),max(x,y)
    print(x,y,max(nb_cycle(a) for a in range(i,j+1)))
