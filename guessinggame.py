n = int(input())
d = [0] * 11
temp = True
while n:
    resp = input()
    if resp == "right on":
        if d[n] == 0:
            d = [0] * 11
            print("Stan may be honest")
        else:
            temp = False
    elif resp == "too high":
        for i in range(n, 11):
            if d[i] == -1:
                temp = False
                break
            d[i] = 1
    elif resp == "too low":
        for i in range(1, 1+n):
            if d[i] == 1:
                temp = False
                break
            d[i] = -1

    if temp == False:
        temp = True
        print("Stan is dishonest")
        while resp != "right on":
            resp = input()
        d = [0] * 11
    n = int(input())
