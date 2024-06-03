l = [i[0] for i in input().split()]
print(max(l.count(i) for i in l))