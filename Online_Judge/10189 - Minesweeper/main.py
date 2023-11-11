n, m = map(int, input().split())
pos = 1
while n or m:
    l = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if l[i][j] != "*":
                r = 0
                # print(i,j, (max(0, i-1), min(n, i+1)), (max(0, j-1), min(j+1,m)))
                for y in range(max(0, i-1), min(n-1, i+1)+1):
                    for x in range(max(0, j-1), min(j+1,m-1)+1):
                        if x != j or y != i:
                            r += l[y][x] == "*"
                l[i][j] = r
    if pos != 1:
        print()
    print(f"Field #{pos}:")
    print("\n".join("".join(str(j) for j in i) for i in l))
    pos += 1
    n, m = map(int, input().split())