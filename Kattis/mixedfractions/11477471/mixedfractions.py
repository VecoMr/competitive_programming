io = open(0)
for i in io:
    a, b = map(int, i.split())
    if b != 0:
        print(a//b, a%b, "/", b)