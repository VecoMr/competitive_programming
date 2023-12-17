l = ["","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

for i in open(0):
    r=[]
    for j in i.strip():
        if j.isalpha():
            for k in range(10):
                if j in l[k]:
                    r.append(str(k))
                    break
        else:
            r.append(j)
    print(*r,sep="")