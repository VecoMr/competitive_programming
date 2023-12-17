a,b,c = 0,0,0
input()
s = input()
t = True
for i in s:
    if i == "(":
        a += 1
    if i == ")":
        a-=1
    if i == "[":
        b += 1
    if i== "]":
        b -= 1
    if i == "{":
        c += 1
    if i == "}":
        c -= 1
    if a < 0 or b < 0 or c < 0:
        t = False
if a or b or c:
    t = False
if t:
    print("Valid")
else:
    print("Invalid")