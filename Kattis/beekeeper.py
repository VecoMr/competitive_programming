n = int(input())
v = "aeiouy"
while n:
    l = []
    for _ in range(n):
        i = input()
        r = 0
        t = ""
        for j in i:
            if j == t and j in v:
                r += 1
            t = j
        l.append([r, i])
    print(max(l)[1])

    n = int(input())