n = int(input())
for _ in range(n):
    b,p = map(float, input().split())
    print(*["%.6f"%(60*(b-i)/p) for i in range(-1, 2)][::-1])