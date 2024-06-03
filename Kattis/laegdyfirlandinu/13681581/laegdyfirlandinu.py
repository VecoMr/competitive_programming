n,m=map(int,input().split())
l = [list(map(int,input().split())) for _ in range(n)]
t = False

for i in range(1, n-1):
    for j in range(1, m-1):
        a = l[i][j]
        if l[i+1][j] > a and l[i-1][j] > a and l[i][j+1] > a and l[i][j-1] > a:
            t = True
            break
    else:
        continue
    break

print(("Neibb", "Jebb")[t])