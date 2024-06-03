x,y,n = map(int,input().split())
for i in range(1, 1+n):
    r = ""
    if i % x == 0:
        r += "Fizz"
    if i % y == 0:
        r += "Buzz"
    if r == "":
        print(i)
    else:
        print(r)
        