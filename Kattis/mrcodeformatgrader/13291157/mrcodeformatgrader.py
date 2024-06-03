n,m=map(int,input().split())
l=list(map(int,input().split()))
e = []
g = []
la = (l[0],l[0])
if l[0] != 1:
    g.append((1, l[0] - 1))

for i in l[1:]:
    if i == la[1] + 1:
        la = (la[0],i)
    else:
        e.append(la)
        g.append((la[1]+1, i-1))
        la = (i,i)
e.append(la)
if la[1] != n:
    g.append((la[1]+1, n))
def printRes(s, l):
    l = [(f"{a}-{b}",str(a))[a==b] for a,b in l]
    if len(l) <= 1:
        print(s,l)
    else:
        print(s,end="")
        print(l[0],end="")
        for i in l[1:-1]:
            print(f", {i}",end="")
        print(f" and {l[-1]}")

printRes("Errors: ", e)
printRes("Correct: ", g)