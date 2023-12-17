import heapq

n = int(input())

while n:
    l = list(map(int, input().split()))
    heapq.heapify(l)
    res = 0
    while len(l) > 1:
        tmp = heapq.heappop(l) + heapq.heappop(l)
        res += tmp
        heapq.heappush(l, tmp)
    print(res)
    n = int(input())