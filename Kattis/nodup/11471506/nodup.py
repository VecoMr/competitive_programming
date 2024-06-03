s = input().split()
print(("no", "yes")[len(s) == len(set(s))])