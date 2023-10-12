import heapq
import itertools

def generate_reports(n, probs):
    reports = list(itertools.product('SCRF', repeat=n))
    return [(report, prod([probs[c] for c in report])) for report in reports]

def prod(lst):
    p = 1
    for x in lst:
        p *= x
    return p

def huffman(report_probs):
    heap = [[wt, [rep, ""]] for rep, wt in report_probs]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

n = int(input())
probs = dict(zip('SCRF', map(float, input().split())))

report_probs = generate_reports(n, probs)

huff_tree = huffman(report_probs)
expected_bits = sum(wt * len(code) for _, (rep, code) in zip(report_probs, huff_tree))

print(f'{expected_bits:.6f}')
