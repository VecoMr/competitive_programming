n = int(input())

for _ in range(n):
    x1, y1, x2, y2 = [ord(i)-(ord("1"), ord("A"))[i.isalpha()] for i in input().split()]
    if (x1+y1)%2 != (x2+y2)%2:
        print("Impossible")
        continue
    if x1 == x2 and y1 == y2:
        print(0, chr(x1 + ord("A")), chr(y1 + ord("1")))
        continue
    l1 = {}
    l2 = {}
    for i in range(-8, 8):
        if 0 <= x1+i < 8 and 0 <= y1+i < 8:
            l1[(x1+i, y1+i)] = True
        if 0 <= x1-i < 8 and 0 <= y1+i < 8:
            l1[(x1-i, y1+i)] = True

    for i in range(-8, 8):
        if 0 <= x2+i < 8 and 0 <= y2+i < 8:
            l2[(x2+i, y2+i)] = True
        if 0 <= x2-i < 8 and 0 <= y2+i < 8:
            l2[(x2-i, y2+i)] = True

    if (x1, y1) in l2:
        print(1, chr(x1 + ord("A")), chr(y1 + ord("1")), chr(x2 + ord("A")), chr(y2 + ord("1")))
        continue
    for i in l1:
        if i in l2:
            print(2, chr(x1 + ord("A")), chr(y1 + ord("1")), chr(i[0] + ord("A")), chr(i[1] + ord("1")), chr(x2 + ord("A")), chr(y2 + ord("1")))
