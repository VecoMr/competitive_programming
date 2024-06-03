import math
d,a,b,h=map(int,open(0))
f=round(((d/2)**2)*math.pi, 4)
s=round(((a+b)/2)*h,4)

if f == s:
    print("Jafn storar!")
elif f > s:
    print("Mahjong!")
else:
    print("Trapizza!")