n,m=open(0)
print(*[i[0] for i in m.split()if i[0].isupper()],sep="")