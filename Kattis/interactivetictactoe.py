import random
from copy import copy

class Tictactoe:
    def __init__(self) -> None:
        self.start = input() == "first"
        self.grid = [list(map(int, input().replace(".", "0").replace("o", "2").replace("x", "1"))) for _ in range(3)]
        self.turn = 0

    def __who_win(self, grid):
        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2] != 0:
                return grid[i][0]
            if grid[0][i] == grid[1][i] == grid[2][i] != 0:
                return grid[0][i]
        if grid[0][0] == grid[1][1] == grid[2][2] != 0:
            return grid[0][0]
        if grid[0][2] == grid[1][1] == grid[2][0] != 0:
            return grid[0][2]
        if sum(grid[i].count(0) for i in range(3)) == 0:
            return 3
        return 0

    def end_grid(self, grid, plays) -> bool:
        me = plays
        p = []
        c_grid = [i[:] for i in grid]
        for i in range(3):
            for j in range(3):
                if c_grid[i][j] == 0:
                    p.append((i, j))
        while p:
            pos = random.choice(p)
            p.remove(pos)
            c_grid[pos[0]][pos[1]] = plays
            plays = int(plays == 1) +1
        print(*c_grid,sep="\n")
        print(self.__who_win(c_grid), me)
        return self.__who_win(c_grid) == me

    def play(self):
        p = {}
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    p[(i, j)] = 0
        print(p)
        for i in p:
            l = copy(self.grid[:])
            l[i[0]][i[1]] = self.start + 1
            for _ in range(1000):
                if self.end_grid(l, self.start + 1):
                    p[i] += 1
            self.grid[i[0]][i[1]] = 0
        print(p)
        print(max(p, key=p.get))

p = Tictactoe()
l = [[0,0,0], [0,0,0], [0,0,0]]
# print(p.end_grid(l, 1))
# print(l)
p.play()