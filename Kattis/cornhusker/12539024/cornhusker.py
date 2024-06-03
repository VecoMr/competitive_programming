l = list(map(int,input().split()))
n, m = map(int,input().split())
print(n*(sum((l[i]*l[i+1]) for i in range(0,10,2))//5)//m)