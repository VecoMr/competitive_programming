a, b = list(input()), list(input())
t = 10
while a and b and t:
    i = b.pop(0)
    if not i in a:
        t -= 1
        continue
    while i in a:
        a.remove(i)
if t:
    if a:
        print("LOSE")
    else:
        print("WIN")
else:
    print("LOSE")