n = int(input())
m = 0
k = 0
t = 0
for i in range(n+2):
    # print(i, k, t)
    if t == n:
        print(k)
        break
    if t + i < n:
        k += 1
        t += i
    elif t + i > n:
        while t + i > n:
            # print(i, k, t, i - k)
            t -= i - k
            k -= 1
        t += i
        k += 1
    else:
        print(k)
        break
