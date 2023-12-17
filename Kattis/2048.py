class Grid:
    def __init__(self, g:list):
        self.g = g

    def __clean_grid(self):
        self.g = [[j for j in i if j] for i in self.g]
        return self.g

    def __complete_grid_from_left(self):
        self.g = [[self.g[i][j] if j < len(self.g[i]) else 0 for j in range(4)] for i in range(4)]
        return self.g

    def move_to_left(self):
        self.__clean_grid()
        r = []
        for i in self.g:
            rt = []
            a = 0
            l = len(i)
            while a < l:
                if a + 1 < l and i[a] == i [a + 1]:
                    rt.append(i[a]+i[a + 1])
                    a += 2
                else:
                    rt.append(i[a])
                    a += 1
            r.append(rt)
        self.g = r
        self.__complete_grid_from_left()

    def left_rotate(self):
        self.g = list(reversed(list(zip(*self.g))))
        return self.g

    def __str__(self):
        return "\n".join(" ".join(str(j) for j in i) for i in self.g)

g = [list(map(int, input().split())) for _ in range(4)]

g = Grid(g)

n = int(input())

for i in range(n):
    g.left_rotate()

g.move_to_left()

for i in range(4 - n):
    g.left_rotate()
print(g)