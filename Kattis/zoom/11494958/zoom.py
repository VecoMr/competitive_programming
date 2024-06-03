n,k = map(int,input().split())
print(*list(map(int,input().split()))[(k-1)::k])