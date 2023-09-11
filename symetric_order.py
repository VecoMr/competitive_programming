n = int(input())
s = 1
while n:
    print(f"SET {s}")
    up = []
    bt = []
    for i in range(n):
        if i%2:
            bt.append(input())
        else:
            up.append(input())
    print(*up,sep="\n")
    print(*bt[::-1],sep="\n")
    n = int(input())
    s += 1
