n,t=map(int,input().split())
l = list(map(int,input().split()))
if t == 1:
    r = "No"
    d = []
    while l:
        i = l.pop(0)
        if l and not i in d:
            d.append(i)
            if 7777 - i in l:
                r = "Yes"
                break
    print(r)
elif t == 2:
    if n == len(set(l)):
        print("Unique")
    else:
        print("Contains duplicate")
elif t == 3:
    l = [i for i in set(l) if l.count(i) > n/2]
    if l:
        print(*l)
    else:
        print(-1)
elif t == 4:
    if n%2:
        print(sorted(l)[n//2])
    else:
        print(*sorted(l)[n//2-1:n//2+1])
elif t == 5:
    print(*sorted([i for i in l if i>=100 and i <= 999]))