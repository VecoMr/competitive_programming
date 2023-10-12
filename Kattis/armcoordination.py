x,y = map(int,input().split())
r = int(input())
h = (2*r**2)**0.5
print(h)
a,b = int(x - h), int(y - h)
c,d = int(x + h), int(y + h)

print(a, b)
print(c, b)
print(c, d)
print(a, d)