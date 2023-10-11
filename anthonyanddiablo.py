import math
a,n=map(float,input().split())
print(("Need more materials!","Diablo is happy!")[0<a<=n**2/(4*math.pi)])