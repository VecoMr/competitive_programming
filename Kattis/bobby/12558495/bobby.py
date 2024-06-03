import math
n = int(input())
for _ in range(n):a,b,x,y,c=map(int,input().split());p=(b-a+1)/b;print(("no","yes")[(c*sum(math.comb(y,i)*p**i*(1-p)**(y-i)for i in range(x,y+1)))>1])