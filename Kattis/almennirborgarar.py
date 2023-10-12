import heapq

n, m = map(int, input().split())
l = sorted([int(i) for i in input().split()])

times = []
for i in range(n-1):
    times.append((l[i+1] - l[i]) * (i + 1))

for t in times:
    if m > t:
        m -= t
    else:
        m = 0
        break

t = [(i, i, 1) for i in l]
heapq.heapify(t)

while m > 0:
    a, b, c = heapq.heappop(t)
    heapq.heappush(t, (a + b, b, c+1))
    m -= 1

print(heapq.heappop(t)[0])
