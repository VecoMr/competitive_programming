import random

l = [chr(random.randint(65, 70))+chr(random.randint(65, 70)) for i in range(20)]
n, m = random.randint(2,10), random.randint(200, 500)
print(n,m)
for _ in range(m):
    i = random.choice(l)
    a = [i]+[random.randint(1,m) for _ in range(n)]
    print(*a)
print(0 ,0)