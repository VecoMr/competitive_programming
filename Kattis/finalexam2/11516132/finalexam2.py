n = int(input())
l = [input() for _ in range(n)]
print(sum(1 for i in range(n-1) if l[i] == l[i+1]))