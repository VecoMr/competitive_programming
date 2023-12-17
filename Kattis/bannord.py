a = input()
b = input()
print(*[(i, "*"*len(i))[sum(1 for j in a if j in i)>0] for i in b.split()])