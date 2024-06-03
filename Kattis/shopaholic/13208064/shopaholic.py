n = int(input())
print(sum(sorted(map(int,input().split()),reverse=True)[2::3]))
