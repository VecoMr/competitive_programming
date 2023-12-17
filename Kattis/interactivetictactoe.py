import random

t = True

def who_win(grid):
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != 0:
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != 0:
            return grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != 0:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != 0:
        return grid[0][2]
    return 0

def is_full(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return False
    return True

def full_random_grid(grid):
    play = 1
    while is_full(grid) == False and who_win(grid) == 0:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if grid[x][y] == 0:
            grid[x][y] = play
            play = 3 - play
    return who_win(grid)

while t:
    s = input()
    if s == " first":
        input()
        input()
        input()
        print(*["...",".x.", "..."], sep="\n")
        continue
    else:
        grid = []
        if s == " second":
            grid = [list(map(int, input()[1:].replace(".","0").replace("o","1").replace("x","2"))) for _ in range(3)]
        else:
            grid = [list(map(int, i.replace(".","0").replace("o","1").replace("x","2"))) for i in [s[1:],input()[1:],input()[1:]]]
        nb_test = 2000
        d = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    tmp = [i[:] for i in grid]
                    tmp[i][j] = 2
                    if who_win(tmp) == 2:
                        d.append((nb_test,i,j))
                        t = False
                        break
                    d.append((sum(full_random_grid([i[:] for i in tmp]) == 2 for _ in range(nb_test)),i,j))
        # print(d)
        if not d:
            t = False
        else:
            d.sort()
            # print(d)
            grid[d[-1][1]][d[-1][2]] = 2
            print(*["".join(".ox"[i] for i in j) for j in grid], sep="\n")
