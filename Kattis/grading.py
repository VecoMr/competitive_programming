a,b,c,d,e = map(int,input().split())
n = int(input())
if n >= a:
    r = "A"
elif n >= b:
    r = "B"
elif n >= c:
    r = "C"
elif n >= d:
    r = "D"
elif n >= e:
    r = "E"
else:
    r = "F"
print(r)