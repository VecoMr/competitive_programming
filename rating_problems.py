n,k = map(int,input().split())
l = [int(input()) for _ in range(k)]
print((sum(l)-3*(n-k))/n, (sum(l)+3*(n-k))/n)