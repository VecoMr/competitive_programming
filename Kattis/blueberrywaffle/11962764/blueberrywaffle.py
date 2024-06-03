a,b=map(int, input().split())
if (b//a)%2:
    if b%a > a//2:
        print("up")
    else:
        print("down")
else:
    if b%a < a//2:
        print("up")
    else:
        print("down")