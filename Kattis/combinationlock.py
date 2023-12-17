s, a, b, c = map(int, input().split())
alpha = 360/40
while s or a or b or c:
    print(int(360*3+(s-a+40)%40*alpha+(b-a+40)%40*alpha+(b-c+40)%40*alpha))
    s, a, b, c = map(int, input().split())