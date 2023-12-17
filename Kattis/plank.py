n = int(input())
r = 0
r += 4**(n//3)
n %= 3
r += (n//2)*2
r += n %2
print(r)