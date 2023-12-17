s = list(input())
a,b=0,0
while s and ((a < 11 or b < 11) or abs(a-b) < 2):
    n,z = s.pop(0), s.pop(0)
    if n == "A":
        a += int(z)
    else:
        b += int(z)
if a > b:
    print("A")
else:
    print("B")