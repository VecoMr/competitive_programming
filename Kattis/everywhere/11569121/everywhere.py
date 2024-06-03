n = int(input())
for i in range(n):
    a = int(input())
    print(len(set([input() for i in range(a)])))
