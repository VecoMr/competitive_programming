l = list(zip(*[list(map(int,input().split())) for _ in range(3)]))
l = [[i for i in j if j.count(i) == 1] for j in l]
print(l[0][0],l[1][0])