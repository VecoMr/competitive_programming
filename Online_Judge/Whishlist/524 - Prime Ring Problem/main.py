import math

d = {}
def isprime(n):
    if n in d:
        return d[n]
    if n == 2 or n == 3:
        d[n] = True
        return True
    if n % 2 == 0 or n < 2:
        d[n] = False
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            d[n] = False
            return False
    d[n] = True
    return True


def solve(l, n, res, kl, k):
    if n == k:
        # print(kl)
        if isprime(kl[(k-1)%n]+kl[k%n]):
            print(*kl)
        return

    for i in l:
        if (not i in kl) and (k < 1 or isprime(i + kl[-1])):
            solve(l, n, res, kl + [i], k + 1)

tmp = 0

for i in [int(i) for i in open(0)]:
    res = []
    if tmp > 0:
        print()
    tmp += 1
    print(f"Case {tmp}:")
    solve(list(range(2, 1+i)), i, res, [1], 1)