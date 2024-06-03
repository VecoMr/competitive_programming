l = [i[:-1] for i in open(0)]
ll = list(map(len,l))
le = max(ll)
print(sum((le-i)**2 for i in ll[:-1]))
