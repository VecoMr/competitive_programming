a,b,c = map(int,input().split())
t = False
if a +b == c:
    print(str(a) + "+" + str(b) + "=" + str(c))
    t = True
if a - b == c and not t:
    print(str(a) + "-" + str(b) + "=" + str(c))
    t = True
if a * b == c and not t:
    print(str(a) + "*" + str(b) + "=" + str(c))
    t = True
if a / b == c and not t:
    print(str(a) + "/" + str(b) + "=" + str(c))
    t = True
if a == b + c and not t:
    print(str(a) + "=" + str(b) + "+" + str(c))
    t = True
if a == b - c and not t:
    print(str(a) + "=" + str(b) + "-" + str(c))
    t = True
if a == b * c and not t:
    print(str(a) + "=" + str(b) + "*" + str(c))
    t = True
if a == b / c and not t:
    print(str(a) + "=" + str(b) + "/" + str(c))
    t = True
