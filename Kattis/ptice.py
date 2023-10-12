a = "ABC"
b = "BABC"
g = "CCAABB"
n = int(input())
s = input()
at = sum(1 for i in range(n) if s[i] == a[i%3])
bt = sum(1 for i in range(n) if s[i] == b[i%4])
gt = sum(1 for i in range(n) if s[i] == g[i%6])
l = sorted([(at, "Adrian"), (bt, "Bruno"), (gt, "Goran")])
print(l[-1][0],*sorted([i[1] for i in l if i[0] == l[-1][0]]),sep="\n")
