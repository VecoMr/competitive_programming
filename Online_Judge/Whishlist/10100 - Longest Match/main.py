import string

l = [i for i in open(0)]
n = len(l)

for i in range(1, n, 2):
    first = l[i-1]
    second = l[i]
    for j in string.punctuation:
        first = first.replace(j, " ")
        second = second.replace(j, " ")
    first = set(first.split())
    second = set(second.split())
    if not first or not second:
        print(f"{str((i//2)+1).rjust(len(str(n//2)), ' ')}. Blank!")
        continue
    r = 0
    if len(second) > len(first):
        first, second = second, first
    for j in second:
        if j in first:
            r += 1
    print(f"{str((i//2)+1).rjust(len(str(n//2)), ' ')}. Length of longest match: {r}")