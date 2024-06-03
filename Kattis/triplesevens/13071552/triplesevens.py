n = input()
t = True
for _ in range(3):
    if not "7" in input():
        t = False
        break

print((0,777)[t])