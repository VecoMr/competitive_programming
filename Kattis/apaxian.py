a,b = input().split()
if a[-1] == "e":
    print(a+"x"+b)
elif a[-1] in "aiou":
    print(a[:-1]+"ex"+b)
elif a[-2:] == "ex":
    print(a+b)
else:
    print(a+"ex"+b)