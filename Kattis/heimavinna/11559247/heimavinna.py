s = input().split(";")
r = 0
for i in s:
    l = list(map(int,i.split("-")))
    if len(l) > 1:
        r += l[1] - l[0] + 1
    else:
        r += 1
print(r)