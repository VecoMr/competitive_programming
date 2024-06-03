n = int(input())
l = list(map(int,input().split()))
u, d = l.pop(-1),1
for i in l[::-1]:
    u,d=d,u
    u,d=i*d+u,d
print(f'{u}/{d}')