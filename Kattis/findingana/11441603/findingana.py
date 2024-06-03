l=list(input())
while l and l[0] != "a":
    l.pop(0)
print(*l,sep="")