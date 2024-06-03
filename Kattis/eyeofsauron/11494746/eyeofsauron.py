s = list(input())
a, b = 0, 0
t = True
while s:
    if s[0] == "|":
        s.pop(0)
        a += 1
    else:
        break

s.pop(0)
s.pop(0)

while s:
    if s[0] == "|":
        s.pop(0)
        b += 1
    else:
        break
if a == b:
    print("correct")
else:
    print("fix")