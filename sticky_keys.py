s = list(input())
a = ""
while s:
    i = s.pop(0)
    if a == "" or a[-1] != i:
        a += i
print(a)