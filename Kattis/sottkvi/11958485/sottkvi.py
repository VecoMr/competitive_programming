a,*l=open(0)
a,b,c=map(int,a.split())
print(sum(1 for i in map(int,l) if i+14 <= b+c))