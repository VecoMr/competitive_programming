n,*l=open(0)
print(sum(1 for i in l if not "CD" in i))