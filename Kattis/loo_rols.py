import math
l,n = map(int,input().split())
print(min(math.ceil(l/n),3))