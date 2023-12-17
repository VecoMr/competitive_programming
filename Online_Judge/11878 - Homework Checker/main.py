res = 0
for i in open(0):
    t,r = i.split("=")
    try:
        a = eval(t)
        if a == int(r):
            res += 1
    except:
        pass
print(res)