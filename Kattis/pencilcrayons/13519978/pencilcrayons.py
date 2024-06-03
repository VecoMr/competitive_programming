n, m = map(int, input().split())
print(sum(m - len(set(input().split())) for _ in range(n)))