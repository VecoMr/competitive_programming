n = int(input())
s = input()
nb_l = 0
n = 1
for i in s:
    if i == "L":
        nb_l += 1
    else:
        print(*list(range(nb_l+n, n-1, -1)),sep="\n")
        n += nb_l+1
        nb_l = 0
print(*list(range(nb_l+n, n-1, -1)),sep="\n")