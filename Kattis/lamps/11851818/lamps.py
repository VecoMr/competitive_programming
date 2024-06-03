inc = [60, 1000, 5]
low = [11, 8000, 60]

def calc(h,p,e):
    return h*p*e/100000

h, p = map(int, input().split())

inc_cost_d = calc(h, p, inc[0])
low_cost_d = calc(h, p, low[0])

inc_cost = 0
low_cost = 0

d = 0

while low_cost >= inc_cost:
    inc_cost += inc_cost_d
    low_cost += low_cost_d
    d += 1
    if (d*h) % inc[1] <= h:
        inc_cost += inc[2]
    if (d*h) % low[1] <= h:
        low_cost += low[2]
print(d)
    