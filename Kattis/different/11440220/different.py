l = [list(map(int, i.split())) for i in open(0)]
for i in l:
    print(abs(i[0] - i[1]))