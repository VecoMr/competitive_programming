s = input()
a, b, c = (1, 0, 0)
for i in s:
    if i == "A":
        a,b = b,a
    if i == "B":
        b,c=c,b
    if i == "C":
        a,c = c,a
print([a,b,c].index(1)+1)