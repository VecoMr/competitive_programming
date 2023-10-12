n = int(input())
for i in range(n):
    a = int(input())
    l = list(map(int,input().split()))
    l = [i for i in l if l.count(i) == 1][0]
    print(f"Case #{i+1}: {l}")