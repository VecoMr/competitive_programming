g, s, c = map(int, input().split())
a = g*3+s*2+c
if a >= 8:
    print("Province or ", end ="")
elif a >= 5:
    print("Duchy or ", end ="")
elif a >= 2:
    print("Estate or ", end ="")

if a >= 6:
    print("Gold")
elif a >= 3:
    print("Silver")
else:
    print("Copper")
