n = int(input())
b = list(bin(n)[2:])
le = len(b)
for i in range(le-1,-1,-1):
    if b[i] == "1":
        break
for j in range(le):
    if b[j] == "1":
        break
print((int("1"+(le-j)*"0",2), n)[i==j], (i-j+1, 0)[i==j])