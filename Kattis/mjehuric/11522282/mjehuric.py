l = list(map(int,input().split()))
a = len(l)

while sum(1 for i in range(a-1) if l[i] > l[i+1]):
    for i in range(a-1):
        if l[i] > l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
            print(*l)