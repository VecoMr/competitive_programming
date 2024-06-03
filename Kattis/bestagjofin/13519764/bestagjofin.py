n, *l = open(0)
l = sorted([[int(i.split()[1]),i.split()[0]] for i in l])
print(l[-1][1])
