n = int(input())
l = [int(input()) for i in range(n)]
c = [l[i] + l[(i-2)%n] for i in range(n)]
print(min(c))