n = int(input())
print(sum((i+1)*j for i,j in enumerate(sorted([float(input().split()[1]) for _ in range(n)], reverse=True))))