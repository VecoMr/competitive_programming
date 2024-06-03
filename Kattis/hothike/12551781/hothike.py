n=int(input())
l=list(map(int,input().split()))
print(*min((max(l[i-2],l[i]), i-1) for i in range(2,n))[::-1])