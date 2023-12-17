t = 0

for i in open(0):
    r = ""
    for j in i:
        if j == '"':
            r += ("``", "''")[t]
            t = (t+1)%2
        else:
            r += j
    print(r,end="")