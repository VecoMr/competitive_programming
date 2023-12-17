n, m = map(int,input().split())
l = [int(input()) for _ in range(n)]
print(("Neibb", "Jebb")[sum(l)<=m])