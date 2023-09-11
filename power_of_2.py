n, e = map(int,input().split())
r = str(2**e)
re = 0
for i in range(int(r),n+1):
    if r in str(i):
        re += 1
print(re)