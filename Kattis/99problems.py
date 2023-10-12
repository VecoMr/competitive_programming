n = int(input())
a = n
b = n

while str(a)[-2:] and str(a)[-2:] != "99":
    a -= 1
while str(b)[-2:] and str(b)[-2:] != "99":
    b += 1
print(sorted([(abs(a-n), -a, a), (abs(b-n), -b, b)])[0][2])
