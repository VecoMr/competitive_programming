n = int(input())
t = 0
while n:
    l1 = sorted([(int(input()), i) for i in range(n)])
    l2 = sorted([int(input()) for _ in range(n)])
    l3 = [i[1] for i in sorted([(l1[i][1], l2[i]) for i in range(n)])]
    if t:
        print()
    t += 1
    print(*l3,sep="\n")
    n = int(input())