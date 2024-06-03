s = int(input())

while s:
    r = 11
    t = sum(int(i) for i in str(s))
    while sum(int(i) for i in str(r*s)) != t:
        r+=1
    print(r)
    s = int(input())
