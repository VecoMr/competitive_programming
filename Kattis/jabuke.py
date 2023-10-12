xa, ya = map(int,input().split())
xb, yb = map(int,input().split())
xc, yc = map(int,input().split())

n = int(input())

l = [[int(i) for i in input().split()] for _ in range(n)]

def calc_area(xa=xa,ya=ya,xb=xb,yb=yb,xc=xc,yc=yc):
    return abs(xa*(yb-yc)+xb*(yc-ya)+xc*(ya-yb))/2

area = calc_area()

print("%.1f" % area)

res = 0

for x, y in l:
    if calc_area(xa=x, ya=y) + calc_area(xb=x, yb=y) + calc_area(xc=x, yc=y) == area:
        res += 1
print(res)