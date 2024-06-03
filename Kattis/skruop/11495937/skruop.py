n = int(input())
v = 7
for _ in range(n):
    s = input()
    if s == "Skru op!" and v < 10:
        v += 1
    if s == "Skru ned!" and v > 0:
        v -= 1
print(v)