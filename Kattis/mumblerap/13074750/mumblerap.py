input()
print(max(map(int, "".join(i if i.isdigit() else " " for i in input()).strip().split())))