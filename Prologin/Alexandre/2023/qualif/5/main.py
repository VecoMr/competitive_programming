n = int(input())
k = int(input())
p = int(input())
l = sorted(list(map(int, input().split())))

su = [p - (l[i+3] - l[i])**2 for i in range(n-3)]

def e(k, c, su, sle, tot):
    if c >= sle or k == 0:
        return tot
    return max(e(k, c+1, su, sle, tot), e(k-1, c+4, su, sle, tot + su[c]))

print(e(k, 0, su, n-3, 0))
