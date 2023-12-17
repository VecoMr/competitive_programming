n = int(input())
l = []
m = 2
while n != 1:
    if n%m==0:
        l.append(m)
        n //= m
    else:
        m += 1
print(len(l))
