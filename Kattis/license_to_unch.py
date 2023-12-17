n = int(input())
print(sorted([(i, j) for i,j in zip(map(int,input().split()), range(n))])[0][1])