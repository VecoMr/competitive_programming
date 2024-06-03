a,l=open(0)
print(["no","yes"][sum(map(int,l.split()))%3<1])