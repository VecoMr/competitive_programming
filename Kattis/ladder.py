import math
h, v = map(int, input().split())
v = math.radians(v)
print(math.ceil(h/math.sin(v)))