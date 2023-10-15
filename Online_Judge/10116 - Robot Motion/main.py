n, m, x = map(int, input().split())

d = {"S" : (0, 1), "W" : (-1, 0), "E": (1, 0), "N" : (0, -1)}

while n or m or x:
    l = [input() for _ in range(n)]
    pos = (x-1, 0)
    turn = 0
    tmp = {pos:turn}
    while True:
        pos = tuple(i+j for i,j in zip(pos, d[l[pos[1]][pos[0]]]))
        turn += 1
        if pos in tmp:
            turn_before = tmp[pos]
            print(f"{turn_before} step(s) before a loop of {turn - turn_before} step(s)")
            break
        if not ((0 <= pos[0] < m) and (0 <= pos[1] < n)):
            print(f"{turn} step(s) to exit")
            break
        tmp[pos] = turn
    n, m, x = map(int, input().split())

