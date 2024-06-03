a,b=input(),list(map(int,input().split()))
print(sum(1 for i in b if i < 0))