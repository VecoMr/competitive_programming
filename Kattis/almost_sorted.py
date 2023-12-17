n = int(input())
l = [int(i) for i in input().split()]
q = int(input())
a = sorted(l)[:q]
for i in a:
    l.remove(i)
print(*a,*l)