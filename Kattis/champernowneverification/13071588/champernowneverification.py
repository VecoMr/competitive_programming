n = input()
tmp = ""
i = 1
while True:
    if n.startswith(tmp+str(i)):
        tmp += str(i)
        i += 1
    else:
        break
if tmp == n:
    print(i-1)
else:
    print(-1)