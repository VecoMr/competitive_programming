n=int(input())
r=0
while n:r+=1;n&=n-1
print(1<<r)