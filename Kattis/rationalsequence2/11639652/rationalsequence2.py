n = int(input())


def find_depth(a,b):
    if a == b:
        return []
    if a > b:
        return find_depth(a-b, b) + [1]
    return find_depth(a, b-a) + [0]

for _ in range(n):
    k, s = input().split()
    a, b = map(int,s.split("/"))
    l = find_depth(a, b)
    le = len(l)
    r = 2**le+sum(2**(le-i-1) for i in range(le) if l[i])
    print(k,r)
