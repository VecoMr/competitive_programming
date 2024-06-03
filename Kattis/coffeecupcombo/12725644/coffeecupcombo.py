n = int(input())
s= input()
res = 0
c = 0
for i in s:
    if i == "1":
        c = 2
        res += 1
    else:
        if c:
            res += 1
            c -= 1
print(res)