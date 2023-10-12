numer = int(input())
r = 0
t = []
while r < 12:
    n,p=input().split()
    if not n in t:
        t.append(n)
        r += 1
        print(n,p)