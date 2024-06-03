n, *l = map(int,open(0))
if len(l)%2:
    print("still running")
else:
    print(sum(l[i+1] - l[i] for i in range(0,len(l),2)))

