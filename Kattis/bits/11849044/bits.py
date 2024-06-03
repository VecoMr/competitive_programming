n,*l=open(0)
print(*[max(bin(int(i[:j])).count("1") for j in range(1, 1+len(i)))for i in l],sep="\n")