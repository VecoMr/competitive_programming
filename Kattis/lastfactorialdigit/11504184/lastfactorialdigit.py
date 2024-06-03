n, *l = map(int,open(0))
for i in l:
    print(eval("*".join(str(j) for j in range(1, i + 1)))%10)