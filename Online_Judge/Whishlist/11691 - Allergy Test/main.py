import math
n = int(input())

def get_sub(l, m, su, c, mc, subl, k):
    if mc == math.floor(m/2):
        return (c, subl)
    if k == m:
        return (math.inf, [])
    su_w, subl_w = get_sub(l, m, su, c + l[k], mc+1, subl + [l[k]], k+1)
    su_o, subl_o = get_sub(l, m, su, c, mc, subl, k+1)
    # print(subl, k, mc, su_w, subl_w, su_o, subl_o)
    if abs(su_w-(su//2)) < abs(su_o-(su//2)):
        return (su_w, subl_w)
    else:
        return (su_o, subl_o)

for _ in range(n):
    m = int(input())
    l = list(map(int,inp1ut().split()))
    su, sub = get_sub(l, m, sum(l), 0, 0, [], 0)
    print(math.ceil(m//2) + sum(sub))
