r=[]
for i in input():
    if i == "<":
        r.pop()
    else:
        r.append(i)
print(*r,sep="")