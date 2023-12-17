while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    l_appel = [list(map(int, input().split()))[2:] for _ in range(n)]
    for _ in range(m):
        i, j = map(int, input().split())
        print(sum(1 for a, b in l_appel if (i < a < i+j or i < a+b < i+j or a < i < a+b or a < i+j < a+b or (a == i and a+b == i+j))))