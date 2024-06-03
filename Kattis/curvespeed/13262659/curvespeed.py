for i in open(0):
    a,b = map(float, i.split())
    print(round(((a*(b+.16))/0.067)**0.5))
