n = 2
la = [1]
lb = [1, 1]
print(1)
print(1,1)

while lb[n//2] < 10**60:
    la = lb
    lb = [1]+[la[i]+la[i+1] for i in range(n-1)]+[1]
    n+=1
    print(*lb)

