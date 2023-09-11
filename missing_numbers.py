n = int(input())
l = set(map(int,[input() for i in range(n)]))
f = [i for i in range(1, max(l)) if i not in l]
if f:
    print(*f, sep="\n")
else:
    print("good job")