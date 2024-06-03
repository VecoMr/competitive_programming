import math

a,b = map(int,(input(),input()))
m = math.ceil(b/a)
r = b - a*(b//a)
if b%a:
    for _ in range(r):
        print("*"*m)
    for _ in range(a-r):
        print("*"*(m-1))
else:
    for i in range(a):
        print("*"*(b//a))