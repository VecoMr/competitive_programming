a,b,c,n=map(int,input().split())
print(("NO","YES")[a and b and c and n>2 and a+b+c >= n])