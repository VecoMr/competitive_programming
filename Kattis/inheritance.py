n = int(input())

l = []

def e(l, k, n):
    if k:
        a = int(k)
        if a > n:
            return
        if n%a == 0:
            l.append(a)
    e(l, k+"2", n)
    e(l, k+"4", n)
e(l, "", n)
print(*sorted(l),sep="\n")