n,*l=open(0)
print(sum(1 for i in l if "rose" in i.lower() or "pink" in i.lower()) or "I must watch Star Wars with my daughter")