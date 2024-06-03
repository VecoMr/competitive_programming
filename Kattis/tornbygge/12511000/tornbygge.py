n = int(input())
l = list(map(int, input().split()))

r = 0
tmp = -1
for i in l:
    if i > tmp:
        r += 1
        tmp = i
    else:
        tmp = i
print(r)