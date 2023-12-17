n = int(input().split())

def is_sort(l):
    a = len(l)
    for i in range(1,a):
        if l[i-1] > l[i]:
            l[i-1]
            return False
    return True

def next_step(l):
    for i in range(1,a):
        if l[i-1] > l[i]:
            
            return False
    return True

for i in range(n):
    a, *l = map(int,input().split())
    while not is_sort(l):
