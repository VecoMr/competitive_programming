import math

n = int(input())
counter = 0
for i in range(n//2, 0, -1):
    counter += 1
    if n % i == 0:
        break
print(counter+n-n//2-1)