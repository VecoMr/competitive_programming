n = int(input())
a,*l = map(int,input().split())

def irreduct(a,b):
    if a == b:
        return [1,1]
    for i in range(2, max(a,b)):
        if a%i == 0 and b%i == 0:
            return irreduct(a//i, b//i)
    return [a, b]

for i in l:
    print(*irreduct(a,i),sep="/")