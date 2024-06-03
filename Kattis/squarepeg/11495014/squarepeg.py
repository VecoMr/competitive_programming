l, r = map(int, input().split())
if (l**2*2)**0.5 <= r*2:
    print("fits")
else:
    print("nope")