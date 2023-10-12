n = int(input())
d = {}

for i in range(1, int(n**(1/3))+1):
    for j in range(1, i+1):
        if i**3+j**3 > n:
            break
        if i**3+j**3 in d:
            d[i**3+j**3] += 1
        else:
            d[i**3+j**3] = 1
d = [i for i in d if d[i] > 1]
if d:
    print(max(d))
else:
    print("none")