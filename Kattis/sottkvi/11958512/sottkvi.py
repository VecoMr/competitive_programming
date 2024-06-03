a,*l=open(0)
a,b,c=map(int,a.split())
print(sum(i+14<=b+c for i in map(int,l)))