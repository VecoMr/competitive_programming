import math

n = int(input())
while n:
    r = []
    for i in range(n):
        x, y, *l = input().split()
        x, y = map(float, [x, y])
        alpha = 0
        for a, b in zip(l[::2], map(float, l[1::2])):
            b = float(b)
            if a == "start":
                alpha = math.radians(b)
            elif a == "walk":
                x, y = x + (b * math.cos(alpha) + b * math.sin(alpha)), y + (-b * math.sin(alpha) + b * math.cos(alpha))
            elif a == "turn":
                alpha += math.radians(b)
        r.append((x,y))
    x, y = 0, 0
    for i in r:
        x += i[0]
        y += i[1]
    print(x/n, y/n)


    n = int(input())