l = [list(input()) for _ in range(3)]
if sum(1 for i in l if "".join(i)=="OOO") or sum(1 for i in list(zip(*l)) if "".join(i)=="OOO") or l[0][0]+l[1][1]+l[2][2]== "OOO" or  l[0][2]+l[1][1]+l[2][0]== "OOO":
    print("Jebb")
else:
    print("Neibb")