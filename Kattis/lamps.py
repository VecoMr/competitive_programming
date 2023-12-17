inc = [60, 1000, 5]
low = [11, 8000, 60]

def calc(h,p,e):
    return h*p*e/100000

h, p = map(int, input().split())

inc_cost_d = calc(h, p, inc[0])
low_cost_d = calc(h, p, low[0])

inc_cost = inc[2]
low_cost = low[2]

inc_h = 0
low_h = 0
d = 0

while low_cost >= inc_cost:
    d += 1
    inc_cost += inc_cost_d
    low_cost += low_cost_d
    inc_h += h
    low_h += h
    if inc_h > inc[1]:
        inc_cost += inc[2]
        inc_h %= inc[1]
    if low_h > low[1]:
        low_cost += low[2]
        low_h %= low[1]
print(d)
    