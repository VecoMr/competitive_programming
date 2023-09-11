a,l=open(0)
print(["no","yes"][sum(map(int,l.split()))%3<1])
# puts`sed 1d`.split.map(&:to_i).sum%3<1?"yes":"no"
