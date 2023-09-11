n,*l = map(int,open(0))
print(*[i//400 + int(i%400!=0) for i in l],sep="\n")