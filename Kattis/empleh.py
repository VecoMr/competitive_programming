w = [i.strip() for i in input()[7:].split(",") if i != ""]
b = [i.strip() for i in input()[7:].split(",") if i != ""]
g = [[(list("..."), list(":::"))[(i+j)%2] for i in range(8)] for j in range(8)]

def print_g(g):
    a = "\n+---+---+---+---+---+---+---+---+\n".join([f'|{"|".join(["".join(i) for i in j])}|' for j in g])
    print("+---+---+---+---+---+---+---+---+", a, "+---+---+---+---+---+---+---+---+",sep="\n")

for i in w:
    n, x, y = None, None, None
    if len(i) == 2:
        n, x, y = "P", ord(i[0]) - ord("a"), int(i[1]) - 1
    elif len(i) == 3:
        n, x, y = i[0].upper(), ord(i[1]) - ord("a") ,int(i[2]) - 1
    g[7-y][x][1] = n

for i in b:
    n, x, y = None, None, None
    if len(i) == 2:
        n, x, y = "p", ord(i[0]) - ord("a"), int(i[1]) - 1
    elif len(i) == 3:
        n, x, y = i[0].lower(), ord(i[1]) - ord("a"), int(i[2]) - 1
    g[7-y][x][1] = n

print_g(g)