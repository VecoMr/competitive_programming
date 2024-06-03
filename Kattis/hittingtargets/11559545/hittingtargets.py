n = int(input())
rect = []
circle = []
for i in range(n):
    name, *l = input().split()
    l = [int(i) for i in l]
    if name == "rectangle":
        rect.append(l)
    if name == "circle":
        circle.append(l)
n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    res = 0
    for j in rect:
        x1, y1, x2, y2 = j
        if (x1 <= x <= x2 or x1 >= x >= x2) and (y1 <= y <= y2 or y1 >= y >= y2):
            res += 1
    for j in circle:
        x1, y1, r = j
        if ((x-x1)**2 + (y-y1)**2 <= r**2):
            res += 1
    print(res)