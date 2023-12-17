n = int(input())

while n:
    l = [input() for _ in range(n)]
    l = sorted([len(i), i, False] for i in l)
    print(l)
    tree = []
    n = int(input())