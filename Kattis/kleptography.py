n, m = map(int,input().split())
a = [ord(i)-ord("a") for i in input()]
b = [ord(i)-ord("a") for i in input()][::-1]
s = ""
for i in range(m):
    s += chr(ord("a") + (b[i] + a[(i%n)]+ 1)%26)
print(s)