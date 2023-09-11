import math
s = input()
l = len(s)
r = int(l**0.5)
c = math.ceil(l/r)
a = [s[i:i+r] for i in range(0,l, r)]
print(*["".join(i) for i in list(zip(*a))],sep="")