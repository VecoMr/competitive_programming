n=int(input())
l = list(map(int,input().split()))
a = sorted(l)
print(sum(a[i] != l[i] for i in range(n)))