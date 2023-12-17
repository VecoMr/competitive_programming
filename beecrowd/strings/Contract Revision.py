a,b=input().split()
while sum(map(int,[a,b])):
    print(int("0"+b.replace(a,"")))
    a, b = input().split()