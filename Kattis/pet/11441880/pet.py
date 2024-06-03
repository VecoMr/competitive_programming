l = [sum(map(int,input().split())) for i in range(5)]
print(l.index(max(l))+1,max(l))