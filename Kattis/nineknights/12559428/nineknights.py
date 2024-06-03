l=[input()for _ in range(5)]
def poss(x,y):
    moves=[]
    if y - 1 >= 0:
        if x - 2 >= 0:
            moves.append((x-2,y-1))
        if x + 2 < 5:
            moves.append((x+2,y-1))
    if y + 1 < 5:
        if x - 2 >= 0:
            moves.append((x-2,y+1))
        if x + 2 < 5:
            moves.append((x+2,y+1))
    if y - 2 >= 0:
        if x - 1 >= 0:
            moves.append((x-1,y-2))
        if x + 1 < 5:
            moves.append((x+1,y-2))
    if y + 2 < 5:
        if x - 1 >= 0:
            moves.append((x-1,y+2))
        if x + 1 < 5:
            moves.append((x+1,y+2))
    return moves

if sum(sum(1 for j in i if j =="k") for i in l) != 9:
    print("invalid")
    exit(0)
for i in range(5):
    for j in range(5):
        if l[j][i] == "k":
            pos = poss(i,j)
            for k,m in pos:
                if l[m][k] == "k":
                    print("invalid")
                    exit(0)
print("valid")
